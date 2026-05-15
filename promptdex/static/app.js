const state = {
  prompts: [],
  categories: [],
  language: localStorage.getItem("promptdex-language") || "es",
  rating: 3,
  favoriteOnly: false,
  copiedId: null,
  expandedIds: new Set(),
  visiblePrompts: [],
};

const selectors = {
  search: document.querySelector("#searchInput"),
  categoryFilter: document.querySelector("#categoryFilter"),
  tagFilter: document.querySelector("#tagFilter"),
  sort: document.querySelector("#sortSelect"),
  languageToggle: document.querySelector("#languageToggle"),
  favoriteFilter: document.querySelector("#favoriteFilter"),
  seedLibrary: document.querySelector("#seedLibrary"),
  exportBackup: document.querySelector("#exportBackup"),
  importBackup: document.querySelector("#importBackup"),
  importFile: document.querySelector("#importFile"),
  list: document.querySelector("#promptList"),
  empty: document.querySelector("#emptyState"),
  count: document.querySelector("#promptCount"),
  template: document.querySelector("#promptCardTemplate"),
  form: document.querySelector("#promptForm"),
  formTitle: document.querySelector("#formTitle"),
  resetForm: document.querySelector("#resetForm"),
  id: document.querySelector("#promptId"),
  title: document.querySelector("#titleInput"),
  category: document.querySelector("#categoryInput"),
  tags: document.querySelector("#tagsInput"),
  body: document.querySelector("#bodyInput"),
  favorite: document.querySelector("#favoriteInput"),
  rating: document.querySelector("#ratingInput"),
};

const translations = {
  es: {
    allCategories: "Todas",
    bodyPlaceholder: "Pega el prompt que quieres guardar.",
    cardsTitle: "Tarjetas",
    categoryLabel: "Categoria",
    clear: "Limpiar",
    close: "Cerrar",
    copied: "Copiado",
    copy: "Copiar",
    delete: "Borrar",
    duplicate: "Duplicar",
    edit: "Editar",
    editPrompt: "Editar prompt",
    emptyHint: "Ajusta filtros o agrega uno nuevo.",
    emptyTitle: "No hay prompts.",
    eyebrow: "Biblioteca local",
    favorite: "Favorito",
    favorites: "Favoritos",
    languageButton: "EN",
    languageLabel: "Cambiar idioma a ingles",
    lastUsedPrefix: "Usado",
    libraryReady: "Biblioteca lista",
    newPrompt: "Nuevo prompt",
    neverUsed: "Nunca usado",
    read: "Leer",
    save: "Guardar",
    searchLabel: "Buscar",
    searchPlaceholder: "Debug agents, landing copy...",
    shortcuts: "Atajos: Ctrl+S guardar, Ctrl+K buscar, Ctrl+Shift+C copiar primera tarjeta.",
    sortFavorites: "Favoritos",
    sortLabel: "Orden",
    sortLastUsed: "Usados",
    sortNewest: "Nuevos",
    sortUpdated: "Actualizados",
    tagLabel: "Etiqueta",
    tagPlaceholder: "codex",
    tagsLabel: "Etiquetas",
    titleLabel: "Titulo",
  },
  en: {
    allCategories: "All categories",
    bodyPlaceholder: "Paste the prompt you want to keep close.",
    cardsTitle: "Prompt cards",
    categoryLabel: "Category",
    clear: "Clear",
    close: "Close",
    copied: "Copied",
    copy: "Copy",
    delete: "Delete",
    duplicate: "Duplicate",
    edit: "Edit",
    editPrompt: "Edit prompt",
    emptyHint: "Adjust filters or add a new keeper.",
    emptyTitle: "No prompts found.",
    eyebrow: "Local prompt index",
    favorite: "Favorite",
    favorites: "Favorites",
    languageButton: "ES",
    languageLabel: "Switch language to Spanish",
    lastUsedPrefix: "Used",
    libraryReady: "Library ready",
    newPrompt: "New prompt",
    neverUsed: "Never used",
    read: "Read",
    save: "Save",
    searchLabel: "Search",
    searchPlaceholder: "Debug agents, landing copy...",
    shortcuts: "Shortcuts: Ctrl+S save, Ctrl+K search, Ctrl+Shift+C copy first card.",
    sortFavorites: "Favorites",
    sortLabel: "Sort",
    sortLastUsed: "Last used",
    sortNewest: "Newest",
    sortUpdated: "Updated",
    tagLabel: "Tag",
    tagPlaceholder: "codex",
    tagsLabel: "Tags",
    titleLabel: "Title",
  },
};

function t(key) {
  return translations[state.language][key];
}

function applyLanguage() {
  document.documentElement.lang = state.language;

  for (const element of document.querySelectorAll("[data-i18n]")) {
    element.textContent = t(element.dataset.i18n);
  }

  for (const element of document.querySelectorAll("[data-i18n-placeholder]")) {
    element.placeholder = t(element.dataset.i18nPlaceholder);
  }

  selectors.languageToggle.textContent = t("languageButton");
  selectors.languageToggle.setAttribute("aria-label", t("languageLabel"));
  selectors.formTitle.textContent = t(
    selectors.formTitle.dataset.mode === "edit" ? "editPrompt" : "newPrompt",
  );
}

async function request(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || `Request failed: ${response.status}`);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

function parseTags(value) {
  return value
    .split(",")
    .map((tag) => tag.trim().toLowerCase())
    .filter(Boolean);
}

function formatDate(value) {
  if (!value) {
    return t("neverUsed");
  }

  return `${t("lastUsedPrefix")} ${new Intl.DateTimeFormat(undefined, {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date(value))}`;
}

function renderRating(container, value, onChange) {
  container.replaceChildren();

  for (let score = 1; score <= 5; score += 1) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `star-button${score <= value ? " active" : ""}`;
    button.textContent = "\u2605";
    button.setAttribute("aria-label", `${score} star${score === 1 ? "" : "s"}`);
    button.addEventListener("click", () => onChange(score));
    container.append(button);
  }
}

function populateCategories() {
  for (const category of state.categories) {
    const filterOption = new Option(category, category);
    const formOption = new Option(category, category);
    selectors.categoryFilter.append(filterOption);
    selectors.category.append(formOption);
  }
}

function promptMatchesFilters(prompt) {
  const search = selectors.search.value.trim().toLowerCase();
  const category = selectors.categoryFilter.value;
  const tag = selectors.tagFilter.value.trim().toLowerCase();

  if (state.favoriteOnly && !prompt.favorite) {
    return false;
  }

  if (category && prompt.category !== category) {
    return false;
  }

  if (tag && !prompt.tags.includes(tag)) {
    return false;
  }

  if (!search) {
    return true;
  }

  return [prompt.title, prompt.body, prompt.category, prompt.tags.join(" ")]
    .join(" ")
    .toLowerCase()
    .includes(search);
}

function renderPrompts() {
  const prompts = state.prompts.filter(promptMatchesFilters);
  state.visiblePrompts = prompts;
  selectors.list.replaceChildren();
  selectors.count.textContent = `${prompts.length} prompt${prompts.length === 1 ? "" : "s"}`;
  selectors.empty.hidden = prompts.length > 0;

  for (const prompt of prompts) {
    const card = selectors.template.content.firstElementChild.cloneNode(true);
    const bodyPreview = card.querySelector(".body-preview");
    const isExpanded = state.expandedIds.has(prompt.id);

    card.querySelector(".badge").textContent = prompt.category;
    card.querySelector("h3").textContent = prompt.title;
    bodyPreview.textContent = prompt.body;
    bodyPreview.classList.toggle("is-expanded", isExpanded);
    card.querySelector(".last-used").textContent = formatDate(prompt.last_used_at);

    const favoriteButton = card.querySelector(".favorite-button");
    favoriteButton.textContent = prompt.favorite ? "\u2605" : "\u2606";
    favoriteButton.classList.toggle("is-favorite", prompt.favorite);
    favoriteButton.addEventListener("click", () =>
      updatePrompt(prompt.id, { favorite: !prompt.favorite }),
    );

    const tags = card.querySelector(".tags");
    for (const tag of prompt.tags) {
      const tagElement = document.createElement("span");
      tagElement.className = "tag";
      tagElement.textContent = `#${tag}`;
      tags.append(tagElement);
    }

    renderRating(card.querySelector(".card-stars"), prompt.rating, (rating) =>
      updatePrompt(prompt.id, { rating }),
    );

    const readButton = card.querySelector(".read-button");
    readButton.textContent = isExpanded ? t("close") : t("read");
    readButton.setAttribute("aria-expanded", String(isExpanded));
    readButton.addEventListener("click", () => togglePromptBody(prompt.id));

    const copyButton = card.querySelector(".copy-button");
    copyButton.textContent = state.copiedId === prompt.id ? t("copied") : t("copy");
    copyButton.addEventListener("click", () => copyPrompt(prompt));

    card.querySelector(".duplicate-button").textContent = t("duplicate");
    card.querySelector(".duplicate-button").addEventListener("click", () => duplicatePrompt(prompt.id));
    card.querySelector(".edit-button").textContent = t("edit");
    card.querySelector(".edit-button").addEventListener("click", () => fillForm(prompt));
    card.querySelector(".delete-button").textContent = t("delete");
    card.querySelector(".delete-button").addEventListener("click", () => deletePrompt(prompt));
    selectors.list.append(card);
  }
}

function togglePromptBody(id) {
  if (state.expandedIds.has(id)) {
    state.expandedIds.delete(id);
  } else {
    state.expandedIds.add(id);
  }
  renderPrompts();
}

function resetForm() {
  selectors.form.reset();
  selectors.id.value = "";
  selectors.formTitle.dataset.mode = "new";
  selectors.formTitle.textContent = t("newPrompt");
  selectors.favorite.checked = false;
  setFormRating(3);
}

function setFormRating(rating) {
  state.rating = rating;
  renderRating(selectors.rating, state.rating, setFormRating);
}

function fillForm(prompt) {
  selectors.id.value = prompt.id;
  selectors.title.value = prompt.title;
  selectors.category.value = prompt.category;
  selectors.tags.value = prompt.tags.join(", ");
  selectors.body.value = prompt.body;
  selectors.favorite.checked = prompt.favorite;
  selectors.formTitle.dataset.mode = "edit";
  selectors.formTitle.textContent = t("editPrompt");
  setFormRating(prompt.rating);
  selectors.title.focus();
}

async function loadPrompts() {
  const params = new URLSearchParams({ sort: selectors.sort.value });
  state.prompts = await request(`/api/prompts?${params}`);
  renderPrompts();
}

async function updatePrompt(id, payload) {
  const updated = await request(`/api/prompts/${id}`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
  state.prompts = state.prompts.map((prompt) => (prompt.id === id ? updated : prompt));
  renderPrompts();
}

async function markUsed(id) {
  const updated = await request(`/api/prompts/${id}/use`, { method: "POST" });
  state.prompts = state.prompts.map((prompt) => (prompt.id === id ? updated : prompt));
  renderPrompts();
}

async function copyPrompt(prompt) {
  await navigator.clipboard.writeText(prompt.body);
  state.copiedId = prompt.id;
  renderPrompts();
  await markUsed(prompt.id);
  window.setTimeout(() => {
    if (state.copiedId === prompt.id) {
      state.copiedId = null;
      renderPrompts();
    }
  }, 1100);
}

async function duplicatePrompt(id) {
  const duplicate = await request(`/api/prompts/${id}/duplicate`, { method: "POST" });
  state.prompts = [duplicate, ...state.prompts];
  selectors.sort.value = "created_desc";
  renderPrompts();
  fillForm(duplicate);
}

async function deletePrompt(prompt) {
  const confirmed = window.confirm(`Delete "${prompt.title}"?`);
  if (!confirmed) {
    return;
  }

  await request(`/api/prompts/${prompt.id}`, { method: "DELETE" });
  state.prompts = state.prompts.filter((item) => item.id !== prompt.id);
  renderPrompts();

  if (selectors.id.value === String(prompt.id)) {
    resetForm();
  }
}

async function seedLibrary() {
  const result = await request("/api/library/seed", { method: "POST" });
  await loadPrompts();
  selectors.seedLibrary.textContent =
    result.imported > 0 ? `+${result.imported} ES/EN` : t("libraryReady");
  window.setTimeout(() => {
    selectors.seedLibrary.textContent = "Biblioteca ES/EN";
  }, 1400);
}

async function exportBackup() {
  const backup = await request("/api/backup/export");
  const blob = new Blob([JSON.stringify(backup, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  const date = new Date().toISOString().slice(0, 10);
  link.href = url;
  link.download = `promptdex-backup-${date}.json`;
  link.click();
  URL.revokeObjectURL(url);
}

async function importBackupFile(file) {
  const text = await file.text();
  const backup = JSON.parse(text);
  await request("/api/backup/import", {
    method: "POST",
    body: JSON.stringify(backup),
  });
  selectors.importFile.value = "";
  await loadPrompts();
}

selectors.form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const payload = {
    title: selectors.title.value,
    body: selectors.body.value,
    category: selectors.category.value,
    tags: parseTags(selectors.tags.value),
    rating: state.rating,
    favorite: selectors.favorite.checked,
  };

  const id = selectors.id.value;
  if (id) {
    await updatePrompt(id, payload);
  } else {
    const created = await request("/api/prompts", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    state.prompts = [...state.prompts, created];
    renderPrompts();
  }

  resetForm();
});

selectors.resetForm.addEventListener("click", resetForm);
selectors.search.addEventListener("input", renderPrompts);
selectors.categoryFilter.addEventListener("change", renderPrompts);
selectors.tagFilter.addEventListener("input", renderPrompts);
selectors.sort.addEventListener("change", loadPrompts);
selectors.languageToggle.addEventListener("click", () => {
  state.language = state.language === "es" ? "en" : "es";
  localStorage.setItem("promptdex-language", state.language);
  applyLanguage();
  renderPrompts();
});
selectors.favoriteFilter.addEventListener("click", () => {
  state.favoriteOnly = !state.favoriteOnly;
  selectors.favoriteFilter.setAttribute("aria-pressed", String(state.favoriteOnly));
  renderPrompts();
});
selectors.seedLibrary.addEventListener("click", seedLibrary);
selectors.exportBackup.addEventListener("click", exportBackup);
selectors.importBackup.addEventListener("click", () => selectors.importFile.click());
selectors.importFile.addEventListener("change", () => {
  const [file] = selectors.importFile.files;
  if (file) {
    importBackupFile(file);
  }
});

document.addEventListener("keydown", (event) => {
  const modifier = event.ctrlKey || event.metaKey;
  const activeElement = document.activeElement;
  const isTyping =
    activeElement instanceof HTMLInputElement || activeElement instanceof HTMLTextAreaElement;

  if (modifier && event.key.toLowerCase() === "s") {
    event.preventDefault();
    selectors.form.requestSubmit();
    return;
  }

  if (modifier && event.key.toLowerCase() === "k") {
    event.preventDefault();
    selectors.search.focus();
    selectors.search.select();
    return;
  }

  if (modifier && event.shiftKey && event.key.toLowerCase() === "c") {
    event.preventDefault();
    const [firstPrompt] = state.visiblePrompts;
    if (firstPrompt) {
      copyPrompt(firstPrompt);
    }
    return;
  }

  if (!isTyping && event.key === "/") {
    event.preventDefault();
    selectors.search.focus();
  }
});

state.categories = await request("/api/categories");
populateCategories();
applyLanguage();
setFormRating(3);
await loadPrompts();
