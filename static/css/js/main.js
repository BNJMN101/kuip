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

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Hero headline: rotate the last word
const rotator = document.querySelector("[data-rotate]");
if (rotator && !reduceMotion) {
  const words = rotator.dataset.rotate.split("|");
  let i = 0;
  setInterval(() => {
    if (document.hidden) return;
    rotator.classList.add("is-out");
    setTimeout(() => {
      i = (i + 1) % words.length;
      rotator.textContent = words[i];
      rotator.classList.remove("is-out");
    }, 280);
  }, 2400);
}

// Demo feed: vote counts tick up
const voteEls = document.querySelectorAll("[data-votes]");
if (voteEls.length && !reduceMotion) {
  setInterval(() => {
    if (document.hidden) return;
    const el = voteEls[Math.floor(Math.random() * voteEls.length)];
    el.textContent = Number(el.textContent) + 1;
    el.classList.remove("pop");
    void el.offsetWidth;
    el.classList.add("pop");
  }, 1400);
}

// Marquee: duplicate the chips so the loop is seamless
document.querySelectorAll("[data-marquee]").forEach((group) => {
  const copy = group.cloneNode(true);
  copy.removeAttribute("data-marquee");
  copy.setAttribute("aria-hidden", "true");
  group.after(copy);
});

// Hero parallax and card tilt (mouse devices only)
const canHover = window.matchMedia("(hover: hover)").matches;
if (canHover && !reduceMotion) {
  const visual = document.querySelector(".lx-visual");
  if (visual) {
    const layers = visual.querySelectorAll("[data-depth]");
    visual.addEventListener("pointermove", (e) => {
      const r = visual.getBoundingClientRect();
      const nx = (e.clientX - r.left) / r.width - 0.5;
      const ny = (e.clientY - r.top) / r.height - 0.5;
      layers.forEach((el) => {
        const depth = Number(el.dataset.depth);
        el.style.transform = `translate3d(${nx * depth}px, ${ny * depth}px, 0)`;
      });
    });
    visual.addEventListener("pointerleave", () => {
      layers.forEach((el) => { el.style.transform = ""; });
    });
  }

  document.querySelectorAll("[data-tilt]").forEach((card) => {
    card.addEventListener("pointermove", (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      card.style.setProperty("--ry", `${px * 10}deg`);
      card.style.setProperty("--rx", `${-py * 10}deg`);
    });
    card.addEventListener("pointerleave", () => {
      card.style.setProperty("--ry", "0deg");
      card.style.setProperty("--rx", "0deg");
    });
  });
}

// Copy-link buttons
document.querySelectorAll("[data-copy]").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const url = window.location.origin + btn.dataset.copy;
    const label = btn.querySelector("span") || btn;
    const original = label.textContent;
    try {
      await navigator.clipboard.writeText(url);
      label.textContent = "Copied";
    } catch (err) {
      window.prompt("Copy this link:", url);
    }
    setTimeout(() => { label.textContent = original; }, 1600);
  });
});