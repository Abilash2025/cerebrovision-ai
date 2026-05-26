import {
    useEffect,
    useRef,
    useState,
} from "react";

import toast
    from "react-hot-toast";

import API
    from "../services/api";

export default function Chatbot({

    prediction,
    confidence,
}) {

    // --------------------------------
    // States
    // --------------------------------

    const [
        messages,

        setMessages
    ] = useState([]);

    const [
        userInput,

        setUserInput
    ] = useState("");

    const [
        loading,

        setLoading
    ] = useState(false);

    // --------------------------------
    // Auto Scroll Ref
    // --------------------------------

    const messagesEndRef =
        useRef(null);

    // --------------------------------
    // Auto Scroll Effect
    // --------------------------------

    useEffect(() => {

        messagesEndRef.current
            ?.scrollIntoView({
                behavior: "smooth",
            });

    }, [messages, loading]);

    // --------------------------------
    // Send Message
    // --------------------------------

    const handleSendMessage =
        async () => {

            if (!userInput.trim()) {

                toast.error(
                    "Please enter a question."
                );

                return;
            }

            try {

                setLoading(true);

                // --------------------------------
                // Add User Message
                // --------------------------------

                const updatedMessages = [

                    ...messages,

                    {
                        role: "user",

                        content:
                            userInput,
                    },
                ];

                setMessages(
                    updatedMessages
                );

                const currentQuestion =
                    userInput;

                setUserInput("");

                // --------------------------------
                // API Request
                // --------------------------------

                const response =
                    await API.post(
                        "/chat",

                        {
                            user_question:
                                currentQuestion,

                            prediction:
                                prediction
                                    ?.predicted_label,

                            confidence:
                                prediction
                                    ?.confidence_score,
                        }
                    );

                // --------------------------------
                // Add AI Response
                // --------------------------------

                setMessages([

                    ...updatedMessages,

                    {
                        role: "assistant",

                        content:
                            response.data
                                .response,
                    },
                ]);

            } catch (err) {

                toast.error(
                    "Chat response failed."
                );

            } finally {

                setLoading(false);
            }
        };

    // --------------------------------
    // Render ChatBot
    // --------------------------------

    return (

        <div
            className="
        mt-10

        w-full
        max-w-3xl
        min-w-3xl

        bg-zinc-900/70

        border
        border-zinc-800

        rounded-2xl

        shadow-2xl

        p-6

        backdrop-blur-md
    "
        >

            {/* Header */}

            <h2
                className="
            text-2xl
            font-semibold
            text-zinc-200

            mb-6
        "
            >
                Chat with CerebroVision
            </h2>

            {/* Messages */}

            <div
                className="
            h-[400px]

            overflow-y-auto
            custom-scrollbar

            flex
            flex-col

            gap-4

            pr-2
        "
            >

                {/* Empty State */}

                <div
                    className={`
                        min-w-full

        ${messages.length === 0

                            ? "visible static"

                            : "invisible absolute"
                        }
    `}
                >

                    <div
                        className="
            text-zinc-500
            text-sm

            flex
            flex-wrap

            gap-3
        "
                    >

                        <button
                            onClick={() =>
                                setUserInput(
                                    "What does this prediction mean?"
                                )
                            }

                            className="
                bg-zinc-800
                hover:bg-zinc-700

                border
                border-zinc-700

                px-4
                py-2

                rounded-xl

                transition
            "
                        >
                            What does this prediction mean?
                        </button>

                        <button
                            onClick={() =>
                                setUserInput(
                                    "How accurate is this prediction?"
                                )
                            }

                            className="
                bg-zinc-800
                hover:bg-zinc-700

                border
                border-zinc-700

                px-4
                py-2

                rounded-xl

                transition
            "
                        >
                            How accurate is this prediction?
                        </button>

                        <button
                            onClick={() =>
                                setUserInput(
                                    "What is Grad-CAM?"
                                )
                            }

                            className="
                bg-zinc-800
                hover:bg-zinc-700

                border
                border-zinc-700

                px-4
                py-2

                rounded-xl

                transition
            "
                        >
                            What is Grad-CAM?
                        </button>

                    </div>

                </div>

                {/* Chat Messages */}

                {
                    messages.map(
                        (
                            message,
                            index
                        ) => (

                            <div
                                key={index}

                                className={`
        max-w-[85%]

        p-4

        rounded-2xl

        whitespace-pre-wrap

        leading-7

        ${message.role === "user"

                                        ? `
                    self-end

                    bg-zinc-200

                    text-black
                `

                                        : `
                    self-start

                    bg-zinc-800

                    text-zinc-200
                `
                                    }
    `}
                            >

                                {message.content}

                            </div>
                        )
                    )
                }

                {/* Loading State */}

                {
                    loading && (

                        <div
                            className="
        self-start

        bg-zinc-800

        text-zinc-300

        px-4
        py-3

        rounded-2xl

        flex
        items-center

        gap-2

    "
                        >

                            <div
                                className="
            w-4
            h-4

            border-2
            border-zinc-400
            border-t-transparent

            rounded-full

            animate-spin
        "
                            />

                            <span>
                                CerebroVision is typing...
                            </span>

                        </div>
                    )
                }

                {/* Auto Scroll Ref */}

                <div ref={messagesEndRef} />

            </div>

            {/* Input Section */}

            <div
                className="
            mt-6

            flex

            gap-3
        "
            >

                <input
                    type="text"

                    value={userInput}

                    onChange={(e) =>
                        setUserInput(
                            e.target.value
                        )
                    }

                    placeholder="
                Ask about the MRI findings...
            "

                    disabled={loading}

                    className="
                flex-1

                bg-zinc-950

                border
                border-zinc-800

                rounded-xl

                px-4
                py-3

                text-zinc-200

                outline-none

                focus:border-zinc-600

                disabled:opacity-50
                disabled:cursor-not-allowed
            "

                    onKeyDown={(e) => {

                        if (
                            e.key === "Enter"
                        ) {

                            handleSendMessage();
                        }
                    }}
                />

                <button
                    onClick={
                        handleSendMessage
                    }

                    disabled={
                        loading ||
                        !userInput.trim()
                    }

                    className="
                bg-zinc-200
                hover:bg-zinc-300

                disabled:opacity-50
                disabled:cursor-not-allowed

                text-black

                px-6

                rounded-xl

                transition

                font-medium
            "
                >

                    {
                        loading
                            ? "Sending..."
                            : "Send"
                    }

                </button>

            </div>

        </div>
    );
}