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
        theme: "ay2",
        maxWidth: 280,
        arrow: true,
        arrowType: "round",
        inertia: true,
        sticky: true,
        placement: "top",
    });
}
