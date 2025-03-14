# Vid2PDF

Vid2PDF is an application that estimates and converts videos into PDF documents. It can also add subtitles if an `.srt` or `.vtt` file is provided. A TTS model support is coming soon.

## Project Setup

1. Clone the repository:
   git clone https://github.com/sarique2003/Vid2pdf.git

2. Install dependencies using Poetry:  
If Poetry is not installed, install it first:
curl -sSL https://install.python-poetry.org | python3 -

3. Activate the virtual environment:
   By typing poetry shell

## How to Use

1. Place your video inside the `tests/videos` folder  
2. Run the following command:  

With subtitles:  
python3 -m src.main tests/videos/<vid_name> -s tests/subtitles/<srt_filename> -o output.pdf

Without subtitles:  
python3 -m src.main tests/videos/input_4.mp4 -o output.pdf
   
