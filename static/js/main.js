let infoTooltips;

(function() {
    initTooltips();
})();

/**
 * Initializes the page tooltips
 */
function initTooltips() {
    infoTooltips = tippy(".info", {
        animation: "scale",
        theme: "ay",
        maxWidth: 400,
        arrow: false,
        inertia: true,
        sticky: true,
        placement: "top",
    });
}
