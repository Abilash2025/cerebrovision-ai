import { Link }
    from "react-router-dom";

export default function LandingPage() {

    return (

        <div
            className="
        min-h-screen

        bg-black

        text-zinc-100

        flex
        flex-col
        items-center
        justify-center

        px-6
    "
        >

            {/* Hero */}

            <div
                className="
            text-center

            max-w-5xl
        "
            >

                <h1
                    className="
                text-6xl
                md:text-7xl

                font-bold

                tracking-tight

                leading-tight
            "
                >

                    CerebroVision AI

                </h1>

                <p
                    className="
                mt-8

                text-xl
                md:text-2xl

                text-zinc-400

                leading-10
            "
                >

                    AI-Assisted Brain Tumor
                    Detection, Explainability,
                    Structured Radiology Reporting,
                    and Intelligent Medical
                    Imaging Insights.

                </p>

                {/* CTA */}

                <Link
                    to="/analyze"
                >

                    <button
                        className="
                    mt-12

                    bg-zinc-100
                    hover:bg-zinc-300

                    text-black

                    px-8
                    py-4

                    rounded-2xl

                    text-lg
                    font-semibold

                    transition
                "
                    >

                        Start MRI Analysis

                    </button>

                </Link>

            </div>

            {/* Feature Chips */}

            <div
                className="
        mt-15

        flex
        flex-col
        items-center
    "
            >

                <h2
                    className="
            text-xl
            md:text-xl

            font-semibold

            text-zinc-300

        "
                >

                    Core Technologies & Features

                </h2>

                <div
                    className="
            flex
            flex-wrap

            items-center
            justify-center


            max-w-24xl
        "
                >
                    <div
                        className="
            mt-10

            flex
            flex-wrap

            items-center
            justify-center

            gap-4

            max-w-4xl
        "
                    >

                        {
                            [

                                "CNN Classification",

                                "Grad-CAM Explainability",

                                "AI Radiology Reports",

                                "Gemini Medical Assistant",

                                "FastAPI Backend",

                                "React Frontend",

                            ].map((feature) => (

                                <div
                                    key={feature}

                                    className="
        px-5
        py-2.5

        rounded-full

        border
        border-zinc-800

        bg-zinc-900/60

        text-sm
        text-zinc-300

        backdrop-blur-md

        hover:border-zinc-700

        transition
    "
                                >

                                    {feature}

                                </div>
                            ))
                        }

                    </div>

                </div>
            </div>
        </div>
    );
}