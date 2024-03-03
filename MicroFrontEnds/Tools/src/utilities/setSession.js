const LOCALHOST_PREFIX = "bot"

const setLocalStorage = (key, value) => {
    localStorage.setItem(LOCALHOST_PREFIX + key, JSON.stringify(value));
}

const getLocalStorage = (key) => {
    const item = localStorage.getItem(LOCALHOST_PREFIX + key);
    if (item)
        return item;
    return '';
}

const clearLocalStorage = () => {
    localStorage.clear();
}

const deleteKeyLocalStorage = (key) => {
    localStorage.removeItem(key);
}

export { setLocalStorage, getLocalStorage, clearLocalStorage, deleteKeyLocalStorage };