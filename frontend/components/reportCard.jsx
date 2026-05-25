import { Download } from "lucide-react";

export default function ReportCard({

  reportSections,

  showReport,

  handleDownloadPDF,

  pdfLoading,
}) {

  if (
    !showReport ||
    !reportSections
  ) {
    return null;
  }

  return (

    <div
      className="
        mt-10
        w-full
        max-w-5xl
        bg-zinc-900/70
        border
        border-zinc-800
        rounded-2xl
        shadow-2xl
        p-8
        backdrop-blur-md
        space-y-8
    "
    >

      <div
        className="
        flex
        items-center
        justify-between
    "
      >

        <h2
          className="
            text-3xl
            font-semibold
            text-zinc-100
        "
        >
          AI Radiology Report
        </h2>

        <button
          onClick={
            handleDownloadPDF
          }

          disabled={
            pdfLoading
          }

          className="
        flex
        items-center
        gap-2

        bg-zinc-800
        hover:bg-zinc-700

        disabled:opacity-50
        disabled:cursor-not-allowed

        border
        border-zinc-700

        px-4
        py-2.5

        rounded-xl

        transition
    "
        >

          {
            pdfLoading ? (

              <>

                <div
                  className="
                        w-4
                        h-4

                        border-2
                        border-zinc-300
                        border-t-transparent

                        rounded-full

                        animate-spin
                    "
                />

                <span
                  className="
                        text-zinc-200
                        text-sm
                        font-medium
                    "
                >
                  Preparing PDF...
                </span>

              </>

            ) : (

              <>

                <Download
                  className="
                        w-5
                        h-5
                        text-zinc-200
                    "
                />

                <span
                  className="
                        text-zinc-200
                        text-sm
                        font-medium
                    "
                >
                  Save as PDF
                </span>

              </>

            )
          }

        </button>

      </div>

      {/* Clinical Context */}

      <div>

        <h3
          className="
                text-xl
                font-semibold
                text-zinc-200
                mb-3
            "
        >
          Clinical Context
        </h3>

        <p
          className="
                text-zinc-400
                leading-8
            "
        >
          {
            reportSections
              .clinical_context
          }
        </p>

      </div>

      {/* Imaging Technique */}

      <div>

        <h3
          className="
                text-xl
                font-semibold
                text-zinc-200
                mb-3
            "
        >
          Imaging Technique
        </h3>

        <p
          className="
                text-zinc-400
                leading-8
            "
        >
          {
            reportSections
              .imaging_technique
          }
        </p>

      </div>

      {/* Findings */}

      <div>

        <h3
          className="
                text-xl
                font-semibold
                text-zinc-200
                mb-3
            "
        >
          AI Findings
        </h3>

        <p
          className="
                text-zinc-400
                leading-8
            "
        >
          {
            reportSections
              .findings
          }
        </p>

      </div>

      {/* Impression */}

      <div
        className="
            bg-zinc-800/80
            border
            border-zinc-700
            rounded-2xl
            p-6
        "
      >

        <h3
          className="
                text-xl
                font-semibold
                text-zinc-100
                mb-3
            "
        >
          Impression
        </h3>

        <p
          className="
                text-zinc-300
                leading-8
            "
        >
          {
            reportSections
              .impression
          }
        </p>

      </div>

      {/* Confidence */}

      <div>

        <h3
          className="
                text-xl
                font-semibold
                text-zinc-200
                mb-4
            "
        >
          Confidence Assessment
        </h3>

        <div
          className="
                grid
                grid-cols-1
                md:grid-cols-3
                gap-4
            "
        >

          <div
            className="
                    bg-zinc-800
                    rounded-xl
                    p-4
                "
          >
            <p
              className="
                        text-zinc-500
                        text-sm
                    "
            >
              Prediction
            </p>

            <p
              className="
                        text-zinc-100
                        text-lg
                        font-medium
                    "
            >
              {
                reportSections
                  .confidence_assessment
                  .prediction
              }
            </p>
          </div>

          <div
            className="
                    bg-zinc-800
                    rounded-xl
                    p-4
                "
          >
            <p
              className="
                        text-zinc-500
                        text-sm
                    "
            >
              Confidence Score
            </p>

            <p
              className="
                        text-zinc-100
                        text-lg
                        font-medium
                    "
            >
              {
                reportSections
                  .confidence_assessment
                  .confidence_score
              }
            </p>
          </div>

          <div
            className="
                    bg-zinc-800
                    rounded-xl
                    p-4
                "
          >
            <p
              className="
                        text-zinc-500
                        text-sm
                    "
            >
              Confidence Level
            </p>

            <p
              className="
                        text-zinc-100
                        text-lg
                        font-medium
                    "
            >
              {
                reportSections
                  .confidence_assessment
                  .confidence_level
              }
            </p>
          </div>

        </div>

      </div>

      {/* Recommendations */}

      <div>

        <h3
          className="
                text-xl
                font-semibold
                text-zinc-200
                mb-3
            "
        >
          Recommendations
        </h3>

        <p
          className="
                text-zinc-400
                leading-8
            "
        >
          {
            reportSections
              .recommendations
          }
        </p>

      </div>

      {/* Disclaimer */}

      <div
        className="
            border-t
            border-zinc-800
            pt-6
        "
      >

        <h3
          className="
                text-lg
                font-semibold
                text-zinc-300
                mb-3
            "
        >
          Disclaimer
        </h3>

        <p
          className="
                text-zinc-500
                text-sm
                leading-7
            "
        >
          {
            reportSections
              .disclaimer
          }
        </p>

      </div>

    </div>

  );
}