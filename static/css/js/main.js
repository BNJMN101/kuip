// Scroll reveal: fade elements in as they enter the screen
document.documentElement.classList.add("js");
const revealItems = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
    const obeserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                obeserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15});
    revealItems.forEach((el) => obeserver.observe(el));
} else {
    revealItems.forEach((el) => el.classList.add('is-visible'));
}

// tabs; switch between panels
document.querySelectorAll("[data-tabs]").forEach((group) => {
    const tabs = group.querySelectorAll("[data-tab]");
    const panels = group.querySelectorAll("[data-panel]");
    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            tabs.forEach((t) => {
                t.classList.toggle("active", t === tab);
                t.setAttribute("aria-selected", t == tab ? "true" : "false");
            });
            panels.forEach((panel) => {
                panel.hidden = panel.dataset.panel != tab.dataset.tab;
            });
        });
    });
});