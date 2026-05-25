import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {Toaster} from "react-hot-toast";
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />

    <Toaster 
      position="top-right"

      toastOptions={{

        style: {
          background:"#18181b",
          color: "#f4f4f5",
          border: "1px solid #27272a",
        },
        success: {
          iconTheme:{
            primary: "#22c55e",
            secondary:"#18181b",
          },
        },
        error: {
          iconTheme:{
            primary:"#ef4444",
            secondary:"#18181b",
          }
        }
      }}

    />

  </StrictMode>,
)
