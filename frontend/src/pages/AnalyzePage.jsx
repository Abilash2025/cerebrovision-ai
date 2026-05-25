import { useState } from "react";
import { useDropzone } from "react-dropzone";
import toast from "react-hot-toast";

import API from "/services/api";

import UploadSection from "/components/UploadSection";
import MRIComparison from "/components/MRIComparison";
import PredictionCard from "/components/PredictionCard";
import ReportCard from "/components/ReportCard";
import ActionButtons from "/components/ActionButtons";
import Chatbot from "/components/Chatbot";


export default function AnalyzePage() {

    // --------------------------------
    // State Management
    // --------------------------------

    const [selectedFile, setSelectedFile] = useState(null);

    const [previewUrl, setPreviewUrl] = useState(null);

    const [prediction, setPrediction] = useState(null);

    const [gradcamImage, setGradcamImage] = useState(null);

    const [reportSections, setReportSections] = useState(null);

    const [showReport, setShowReport] = useState(false);

    const [loading, setLoading] = useState(false);

    const [gradcamLoading, setGradcamLoading] = useState(false);

    const [reportLoading, setReportLoading] = useState(false);

    const [showChatbot, setShowChatbot] = useState(false);

    const [showGradcam, setShowGradcam] = useState(false);

    const [uploadedImagePath, setUploadedImagePath] = useState(null);

    const [gradcamImagePath, setGradcamImagePath] = useState(null);

    const [pdfLoading, setPdfLoading] = useState(false);

    // --------------------------------
    // File Upload
    // --------------------------------

    const onDrop = (acceptedFiles) => {

        const file = acceptedFiles[0];

        if (!file) return;

        setSelectedFile(file);

        setPreviewUrl(
            URL.createObjectURL(file)
        );

        setPrediction(null);

        setGradcamImage(null);

        setReportSections(null);

        setShowChatbot(false);

        setShowReport(false);
    };


    const {
        getRootProps,
        getInputProps,
    } = useDropzone({
        onDrop,
        accept: {
            "image/*": [],
        },
        multiple: false,
    });


    // --------------------------------
    // Prediction Request
    // --------------------------------

    const handlePrediction =
        async () => {

            if (!selectedFile) return;

            setLoading(true);

            try {

                const formData =
                    new FormData();

                formData.append(
                    "file",
                    selectedFile
                );

                const response =
                    await API.post(
                        "/predict",
                        formData,
                        {
                            headers: {
                                "Content-Type":
                                    "multipart/form-data",
                            },
                        }
                    );

                setPrediction(
                    response.data.result
                );

                setUploadedImagePath(response.data.image_path);

                toast.success(
                    "MRI analyzed successfully."
                )

            } catch (err) {

                toast.error(
                    "Prediction failed."
                );

            } finally {

                setLoading(false);
            }
        };



    const ensureGradcamExists =
        async () => {

            // --------------------------------
            // Reuse Existing Grad-CAM
            // --------------------------------

            if (gradcamImagePath) {

                return {

                    url:
                        gradcamImage,

                    localPath:
                        gradcamImagePath,
                };
            }

            try {

                // --------------------------------
                // Prepare Form Data
                // --------------------------------

                const gradcamFormData =
                    new FormData();

                gradcamFormData.append(
                    "file",
                    selectedFile
                );

                // --------------------------------
                // Generate Grad-CAM
                // --------------------------------

                const response =
                    await API.post(
                        "/gradcam",
                        gradcamFormData
                    );

                const gradcamUrl =
                    response.data
                        .gradcam_url;

                const gradcamLocalPath =
                    response.data
                        .gradcam_local_path;

                // --------------------------------
                // Cache Grad-CAM
                // --------------------------------

                setGradcamImage(
                    gradcamUrl
                );

                setGradcamImagePath(
                    gradcamLocalPath
                );

                return {

                    url:
                        gradcamUrl,

                    localPath:
                        gradcamLocalPath,
                };

            } catch (err) {

                toast.error(
                    "Grad-CAM generation failed."
                );

                throw err;
            }
        };
    // GradCAM Request
    // --------------------------------

    const handleGradcam =
        async () => {

            try {

                if (!prediction) {

                    toast.error(
                        "Please make a prediction first."
                    );

                    return;
                }

                // --------------------------------
                // Ensure Grad-CAM Exists
                // --------------------------------

                const gradcamData = await ensureGradcamExists();

                // --------------------------------
                // Show Grad-CAM only when User requests
                // --------------------------------
                setGradcamImage(gradcamData.url);

                setShowGradcam(true);

                toast.success(
                    "Gradcam generated successfully."
                )

            } catch (err) {

                toast.error(
                    "Grad-CAM generation failed."
                );
            }
        };

    // --------------------------------
    // Report Generation
    // --------------------------------

    const handleGenerateReport =
        async () => {

            try {

                if (!prediction) {

                    toast.error(
                        "Please make a prediction first."
                    );

                    return;
                }

                // --------------------------------
                // Hide Existing Report
                // --------------------------------

                if (showReport) {

                    setShowReport(false);

                    return;
                }

                // --------------------------------
                // Use Cached Report
                // --------------------------------

                if (reportSections) {

                    setShowReport(true);

                    return;
                }

                // --------------------------------
                // Generate Report
                // --------------------------------

                const response =
                    await API.post(
                        "/generate-report",

                        {
                            prediction:
                                prediction
                                    .predicted_label,

                            confidence:
                                prediction
                                    .confidence_score,
                        }
                    );

                setReportSections(
                    response.data
                        .report_sections
                );

                setShowReport(true);

                toast.success(
                    "Report generated successfully."
                )

            } catch (err) {

                toast.error(
                    "Failed to generate report."
                );
            }
        };
    const handleToggleChatbot =
        () => {

            if (!prediction) {

                toast.error(
                    "Please generate a prediction first."
                );

                return;
            }

            setShowChatbot(
                (prev) => !prev
            );
        };


    // --------------------------------
    // Handle Download
    // --------------------------------

    const handleDownloadPDF =
        async () => {

            setPdfLoading(true);

            try {

                const gradcamData =
                    await ensureGradcamExists();

                const response =
                    await API.post(
                        "/generate-pdf",

                        {
                            prediction:
                                prediction
                                    .predicted_label,

                            confidence:
                                prediction
                                    .confidence_score,

                            report_sections:
                                reportSections,

                            original_mri_path:
                                uploadedImagePath,

                            gradcam_local_path:
                                gradcamData.localPath,
                        },

                        {
                            responseType:
                                "blob",
                        }
                    );

                const blob =
                    new Blob(
                        [response.data],
                        {
                            type:
                                "application/pdf",
                        }
                    );

                const url =
                    window.URL
                        .createObjectURL(
                            blob
                        );

                const link =
                    document
                        .createElement(
                            "a"
                        );

                link.href = url;

                link.download =
                    "cerebrovision_report.pdf";

                document.body
                    .appendChild(
                        link
                    );

                link.click();

                link.remove();

                window.URL
                    .revokeObjectURL(
                        url
                    );

                toast.success(
                    "PDF downloaded successfully."
                )
            } catch (err) {

                toast.error(
                    "PDF download failed."
                );
            }
            finally {

                setPdfLoading(false);
            }
        };
    // --------------------------------
    // Reset State
    // --------------------------------

    const handleReset = async () => {

        //clean backend state
        try {

            await API.post(
                "/cleanup",
                [
                    uploadedImagePath,
                    gradcamImagePath,
                ]
            )
        } catch (err) {
            console.error(
                "Backend Cleanup failed",
                err
            );

        }

        //Cleanup frontend state
        setSelectedFile(null);

        setPreviewUrl(null);

        setPrediction(null);

        setGradcamImage(null);

        setReportSections(null);

        setShowChatbot(false);

        setShowReport(false);
    };


    return (

        <div className="
      min-h-screen
      bg-gradient-to-br
      from-zinc-950
      via-stone-900
      to-zinc-950
      text-white
      flex
      flex-col
      items-center
      p-8
    ">

            {/* Header */}

            <h1 className="
        text-5xl
        font-bold
        text-zinc-200
        mb-3
        mt-3
      ">
                CerebroVision AI
            </h1>

            <p className="
        text-zinc-500
        mb-10
        text-center
        max-w-xl
        mt-1
      ">
                Explainable Vision-Language AI
                System for Brain Tumor Analysis
                and Radiology Report Generation
            </p>


            {/* Upload OR MRI */}

            {
                previewUrl ? (

                    <div className="
            flex
            flex-col
            items-center
            gap-8
          ">

                        <MRIComparison
                            previewUrl={previewUrl}
                            gradcamImage={
                                showGradcam
                                    ? gradcamImage
                                    : null
                            }
                        />

                        <p className="
              text-zinc-500
              text-sm
            ">
                            {selectedFile?.name}
                        </p>

                        <ActionButtons
                            handlePrediction={
                                handlePrediction
                            }
                            handleGradcam={
                                handleGradcam
                            }
                            handleGenerateReport={
                                handleGenerateReport
                            }
                            handleReset={
                                handleReset
                            }
                            loading={
                                loading
                            }
                            gradcamLoading={
                                gradcamLoading
                            }
                            reportLoading={
                                reportLoading
                            }
                            showReport={
                                showReport
                            }
                            reportSections={
                                reportSections
                            }
                            showChatbot={
                                showChatbot
                            }
                            handleToggleChatbot={
                                handleToggleChatbot
                            }
                        />

                    </div>

                ) : (

                    <UploadSection
                        getRootProps={
                            getRootProps
                        }
                        getInputProps={
                            getInputProps
                        }
                    />
                )
            }



            {/* Prediction */}

            <PredictionCard
                prediction={prediction}
            />


            {/* Report */}

            <ReportCard
                reportSections={
                    reportSections
                }

                showReport={
                    showReport
                }

                handleDownloadPDF={
                    handleDownloadPDF
                }

                pdfLoading={
                    pdfLoading
                }
            />

            {/* Chatbot */}
            {
                prediction
                && showChatbot && (

                    <Chatbot
                        prediction={prediction}
                    />
                )
            }
        </div>

    );
}

