function UploadSection({
  getRootProps,
  getInputProps,
}) {

  return (
    <div>
    <div
      {...getRootProps()}
      className="
        border-2
        border-dashed
        border-zinc-700
        bg-zinc-900/40
        rounded-2xl
        p-12
        w-full
        max-w-lg
        text-center
        cursor-pointer
        hover:bg-zinc-800/50
        transition
        backdrop-blur-sm
      "
    >

      <input {...getInputProps()} />

      <p className="
        text-zinc-300
        text-lg
      ">
        Drag & Drop MRI Image
      </p>

      <p className="
        text-zinc-500
        mt-2
        text-sm
      ">
        or click to browse files
      </p>

    </div>
    <div
        className="
        mt-4

        w-full
        max-w-3xl

        bg-zinc-900/60

        border
        border-zinc-800

        rounded-xl

        p-4

        flex
        flex-col
        items-center
        justify-center

        text-center
    "
      >

        <p
          className="
            text-sm
            text-zinc-400
        "
        >
          No MRI scan available?
          Download a sample MRI image to test the application.
        </p>

        <a
          href="/test-images/sample-mri.jpg"
          download = "sample-mri.jpg"

          className="
            inline-flex
            items-center
    
            mt-3

            px-4
            py-2

            rounded-lg

            bg-zinc-600
            hover:bg-zinc-800

            text-white
            text-sm

            transition
        "
        >
          Download Sample MRI
        </a>

      </div>
      </div>

  );
}

export default UploadSection;
