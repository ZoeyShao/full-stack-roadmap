(function () {
  function applyCourseTraceMode() {
    var isRaw = new URLSearchParams(window.location.search).has("raw");

    document.documentElement.classList.toggle("course-trace-rendered", !isRaw);
    document.documentElement.classList.toggle("course-trace-raw", isRaw);
  }

  function getLectureLabel() {
    var trace = new URLSearchParams(window.location.search).get("trace") || "";
    var match = trace.match(/lecture_(\d+)/);

    if (match) {
      return "Lecture " + match[1];
    }

    return trace.split("/").pop().replace(/\.json$/, "") || "Trace";
  }

  function updateCourseHeader() {
    var title = document.querySelector(".header-title > span:first-child");
    var heading = document.querySelector(".markdown h1");

    if (!title) {
      return;
    }

    var nextTitle = getLectureLabel();

    if (heading && heading.textContent.trim()) {
      nextTitle += " · " + heading.textContent.trim();
    }

    if (title.textContent !== nextTitle) {
      title.textContent = nextTitle;
    }
  }

  function patchHistoryMethod(methodName) {
    var original = window.history[methodName];

    window.history[methodName] = function () {
      var result = original.apply(this, arguments);
      applyCourseTraceMode();
      updateCourseHeader();
      window.setTimeout(applyCourseTraceMode, 0);
      window.setTimeout(updateCourseHeader, 0);
      return result;
    };
  }

  function startCoursePolish() {
    if (!document.body) {
      return;
    }

    updateCourseHeader();

    new MutationObserver(updateCourseHeader).observe(document.body, {
      childList: true,
      subtree: true,
    });
  }

  function safeTypeset() {
    var mathJax = window.MathJax;

    if (mathJax && typeof mathJax.typesetPromise === "function") {
      mathJax.typesetPromise().catch(function (error) {
        console.warn("MathJax typeset failed", error);
      });
    }
  }

  window.MathJax = window.MathJax || {};
  window.MathJax.typeset =
    typeof window.MathJax.typeset === "function"
      ? window.MathJax.typeset
      : safeTypeset;

  applyCourseTraceMode();
  patchHistoryMethod("pushState");
  patchHistoryMethod("replaceState");
  window.addEventListener("popstate", applyCourseTraceMode);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startCoursePolish);
  } else {
    startCoursePolish();
  }
})();
