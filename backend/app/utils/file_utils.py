import os
from fastapi import HTTPException


def cleanup_files():
    try:

        folders = [

            "tmp/uploads",

            "tmp/gradcam",

            "tmp/reports",
        ]

        for folder in folders:

            if os.path.exists(folder):

                for file in os.listdir(folder):

                    file_path = os.path.join(
                        folder,
                        file
                    )

                    if os.path.isfile(file_path):

                        os.remove(file_path)

        return {
            "success": True
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )