
import fastbook
fastbook.setup_book()
import os
from fastbook import *



categories=["Darth Vader", "Yoda", "Luke Skywalker", "R2D2", "C3PO"]
if not os.path.exists("images"):
    os.makedirs("images")
    

for category in categories:
    directory_path = "images/"+category.replace(" ", "_")
    category_name = category.replace(" ","")
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    results = search_images_ddg(category, max_images=150)
    img_number=1
    for index, link in enumerate(results):
        print(index)
        #dest = f"{category}_duckduckgo_{ind}.jpg"
        try:

            response = requests.get(link, timeout=10)
            print(response.status_code)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract the file extension from the URL
                file_extension = link.split('.')[-1]
                if file_extension in ["jpeg", "jpg", "png"]:
                    # Save the image to a file with a unique name
                    filename = f"{category_name}_duckduckgo_{img_number}.{file_extension}"
                    filepath = os.path.join(directory_path, filename)
                # print(response.iter_content(chunk_size=128))
                    with open(filepath, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=128):
                            file.write(chunk)
                
                    print(f"Image {index + 1} downloaded: {filename}")
                    img_number+=1
            else:
                print(f"Invalid response status: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {index}: {str(e)}")
            continue