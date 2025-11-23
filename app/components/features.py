import reflex as rx


def feature_item(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-8 w-8 text-[#FFB800]"),
            class_name="flex items-center justify-center h-16 w-16 mb-6 bg-[#FFB800]/10 border border-[#FFB800]/50 shadow-[0_0_15px_rgba(255,184,0,0.3)] clip-path-polygon-[50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%]",
        ),
        rx.el.h3(
            title,
            class_name="text-xl leading-6 font-bold text-white font-['Rajdhani'] uppercase tracking-wider",
        ),
        rx.el.p(description, class_name="mt-3 text-base text-gray-400 leading-relaxed"),
        class_name="p-8 bg-gradient-to-b from-white/5 to-transparent backdrop-blur-sm border border-white/10 hover:border-[#FFB800]/50 transition-all duration-500 hover:shadow-[0_0_30px_rgba(255,184,0,0.1)] group",
    )


def features() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(74,37,17,0.2)_0%,rgba(0,0,0,0)_60%)] pointer-events-none"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "CORE PROTOCOLS",
                    class_name="text-sm text-[#FFB800] font-mono font-bold tracking-[0.3em] uppercase mb-2",
                ),
                rx.el.p(
                    "WHY CHOOSE PLEROMA GOLD?",
                    class_name="mt-2 text-3xl leading-8 font-bold tracking-tight text-white sm:text-4xl font-['Rajdhani'] drop-shadow-[0_0_10px_rgba(255,255,255,0.3)]",
                ),
                rx.el.p(
                    "Dedicated to extracting the finest natural essence. Ethically sourced, molecularly preserved for maximum nutrition and quantum flavor profile.",
                    class_name="mt-4 max-w-2xl text-xl text-gray-400 lg:mx-auto",
                ),
                class_name="lg:text-center mb-16 relative z-10",
            ),
            rx.el.div(
                rx.el.div(
                    feature_item(
                        "leaf",
                        "100% BIOLOGICAL",
                        "Zero artificial interference. Pure, unadulterated wholesome goodness extracted directly from nature's source code.",
                    ),
                    feature_item(
                        "clock",
                        "FRESHNESS SYNC",
                        "Groundnuts processed daily in micro-batches to guarantee optimal freshness synchronization.",
                    ),
                    feature_item(
                        "shield-check",
                        "QUALITY SHIELD",
                        "Absolute satisfaction protocol. We stand behind our products with a complete quality guarantee.",
                    ),
                    class_name="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3",
                ),
                class_name="mt-10 relative z-10",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="py-24 bg-[#0A0A0C] relative overflow-hidden border-b border-[#FFB800]/10",
        id="about",
    )