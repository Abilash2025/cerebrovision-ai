function PredictionCard({
  prediction,
}) {

  if (!prediction) return null;

  const confidence = prediction?.confidence_score || 0;

  const confidenceColor =
    confidence >= 85
      ? "bg-green-500"
      : confidence >= 75
        ? "bg-yellow-500"
        : "bg-red-500"

  const confidenceLabel =
    confidence >= 95
      ? "Very High"
      : confidence >= 85
        ? "High"
        : confidence >= 75
          ? "Moderate"
          : "Low"

  return (

    <div className="
      mt-10
      bg-zinc-900/70
      border
      border-zinc-800
      backdrop-blur-md
      p-5
      rounded-2xl
      shadow-2xl
      w-full
      max-w-sm
    ">

      <h2 className="
        text-xl
        font-semibold
        mb-5
        text-zinc-200
      ">
        Prediction Result
      </h2>

      <div className="
        space-y-4
      ">

        <div>

          <p className="
            text-zinc-500
            text-sm
          ">
            Tumor Type
          </p>

          <p className="
            text-lg
            font-medium
            capitalize
          ">
            {
              prediction.predicted_label
            }
          </p>

        </div>


        <div>

          <p className="
            text-zinc-500
            text-sm
          ">
            Confidence Score
          </p>

          <p className="
            text-lg
            font-medium
            text-emerald-300
          ">
            {
              prediction.confidence_score
            }%
          </p>

          {/* Confidence Bar */}

          <div
            className="
        mt-5
        w-full
    "
          >

            {/* Labels */}

            <div
              className="
            flex
            items-center
            justify-between

            mb-2
        "
            >

              <span
                className="
                text-sm
                text-zinc-400
            "
              >
                Confidence Level
              </span>

              <span
                className="
                text-sm
                font-medium
                text-zinc-300
            "
              >
                {confidenceLabel}
              </span>

            </div>

            {/* Progress Track */}

            <div
              className="
            w-full
            h-3

            bg-zinc-800

            rounded-full

            overflow-hidden
        "
            >

              {/* Animated Fill */}

              <div
                className={`
                h-full

                ${confidenceColor}

                transition-all
                duration-700
                ease-out

                rounded-full
            `}
                style={{
                  width:
                    `${confidence}%`
                }}
              />

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default PredictionCard;