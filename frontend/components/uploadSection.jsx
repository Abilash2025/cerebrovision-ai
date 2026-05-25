function UploadSection({
  getRootProps,
  getInputProps,
}) {

  return (

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
  );
}

export default UploadSection;