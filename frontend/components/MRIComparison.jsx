function MRIComparison({
  previewUrl,
  gradcamImage,
}) {

  return (

    <div className="
      flex
      flex-wrap
      justify-center
      gap-8
    ">

      {/* Original MRI */}

      <div className="
        flex
        flex-col
        items-center
      ">

        <h2 className="
          text-zinc-300
          text-lg
          mb-4
        ">
          Original MRI
        </h2>

        <img
          src={previewUrl}
          alt="MRI Preview"
          className="
            w-[220px]
            rounded-2xl
            shadow-2xl
            border
            border-zinc-800
            object-cover
          "
        />

      </div>


      {/* GradCAM */}

      {
        gradcamImage && (

          <div className="
            flex
            flex-col
            items-center
          ">

            <h2 className="
              text-zinc-300
              text-lg
              mb-4
            ">
              Highlighted Tumor Regions
            </h2>

            <img
              src={gradcamImage}
              alt="GradCAM"
              className="
                w-[220px]
                rounded-2xl
                shadow-2xl
                border
                border-zinc-800
                object-cover
              "
            />

          </div>
        )
      }

    </div>
  );
}

export default MRIComparison;