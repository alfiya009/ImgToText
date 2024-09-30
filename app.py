# import gradio as gr
# from PIL import Image
# import pytesseract

# # Function to perform OCR and keyword search
# def ocr_and_search(image, keyword):
#     # Perform OCR on the uploaded image
#     text = pytesseract.image_to_string(image, lang='eng+hin')
    
#     # Perform a simple search for the keyword
#     if keyword:
#         results = [line for line in text.split('\n') if keyword.lower() in line.lower()]
#     else:
#         results = []
        
#     # Return the extracted text and search results
#     return text, "\n".join(results)

# # Gradio Interface for the web application
# iface = gr.Interface(
#     fn=ocr_and_search,
#     inputs=[gr.Image(type="pil", label="Upload Image"), 
#             gr.Textbox(label="Enter keyword to search")],
#     outputs=["textbox", "textbox"],
#     title="OCR with Keyword Search",
#     description="Upload an image containing both Hindi and English text, extract the text, and search for keywords."
# )

# # Launch the app
# iface.launch()

import gradio as gr
from PIL import Image
import pytesseract

# Function to perform OCR and keyword search
def ocr_and_search(image, keyword):
    # Perform OCR on the uploaded image
    text = pytesseract.image_to_string(image, lang='eng+hin')
    
    # Perform a simple search for the keyword
    if keyword:
        results = [line for line in text.split('\n') if keyword.lower() in line.lower()]
    else:
        results = []
        
    # Return the extracted text and search results
    return text, "\n".join(results)

# Gradio Interface for the web application with an enhanced UI
with gr.Blocks() as iface:
    gr.Markdown(
        """
        # Hindi-English OCR with Keyword Search
        Upload an image containing text in **Hindi** and **English**. The app will extract the text, and you can search for specific keywords within the extracted text.
        """
    )
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Image", show_label=True)
            keyword_input = gr.Textbox(label="Enter Keyword to Search", placeholder="Type keyword here...")
            submit_button = gr.Button("Extract and Search")
        
        with gr.Column():
            extracted_text_output = gr.Textbox(label="Extracted Text", placeholder="Text will be shown here...", lines=10)
            search_results_output = gr.Textbox(label="Search Results", placeholder="Search results will be shown here...", lines=10)
    
    submit_button.click(ocr_and_search, [image_input, keyword_input], [extracted_text_output, search_results_output])

# Launch the app
iface.launch(share=True)


