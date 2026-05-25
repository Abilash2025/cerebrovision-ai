
function ActionButtons({
  handlePrediction,
  handleGradcam,
  handleGenerateReport,
  handleReset,
  handleToggleChatbot,
  loading,
  gradcamLoading,
  reportLoading,
  showChatbot,
  showReport,
  reportSections,
}) {

  return (

    <div className="
      flex
      flex-wrap
      justify-center
      gap-4
    ">

      <button
        onClick={handlePrediction}
        disabled={loading}
        className="
          bg-zinc-200
          hover:bg-zinc-300
          text-black
          px-6
          py-3
          rounded-xl
          font-medium
          transition
          shadow-lg
        "
      >

        {
          loading
            ? "Analyzing..."
            : "Predict Tumor"
        }

      </button>


      <button
        onClick={handleGradcam}
        disabled={gradcamLoading}
        className="
          bg-zinc-800
          hover:bg-zinc-700
          px-6
          py-3
          rounded-xl
          transition
          border
          border-zinc-700
        "
      >

        {
          gradcamLoading
            ? "Generating..."
            : "Show Highlighted Tumor Regions"
        }

      </button>


      <button
        onClick={handleGenerateReport}
        disabled={reportLoading}
        className="
          bg-zinc-900
          hover:bg-zinc-800
          px-6
          py-3
          rounded-xl
          transition
          border
          border-zinc-700
        "
      >

        {
          !reportSections
          ? "Generate Report"

          :showReport
            ? "Hide Report"
            : "Show Report"
        }

      </button>

      <button
        onClick={handleToggleChatbot}
        className="
    bg-zinc-800
    hover:bg-zinc-700
    px-6
    py-3
    rounded-xl
    transition
    border
    border-zinc-700
  "
      >
        {
          showChatbot
            ? "Hide Chatbot"
            : "Chat with CerebroVision"
        }
      </button>

      <button
        onClick={handleReset}
        className="
          bg-zinc-950
          hover:bg-zinc-900
          px-5
          py-3
          rounded-xl
          transition
          border
          border-zinc-800
        "
      >
        Upload Another MRI
      </button>

    </div>
  );
}

export default ActionButtons;