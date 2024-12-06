# First step : Filter the duplicated data from 300 testing datasets
# import pandas as pd

# # Function to combine two CSV files based on imageID and remove duplicates
# def combine_csv(training_csv, testing_csv, output_csv, image_id_column='Image ID'):
#     # Load the CSV files
#     training_df = pd.read_csv(training_csv)
#     testing_df = pd.read_csv(testing_csv)
    
#     # Check if the imageID column exists in both CSVs
#     if image_id_column not in training_df.columns or image_id_column not in testing_df.columns:
#         print(f"Column '{image_id_column}' not found in one or both CSVs.")
#         return
    
#     # Merge both DataFrames on the 'imageID' column
#     combined_df = pd.concat([training_df, testing_df], ignore_index=True)
    
#     # Find duplicate imageIDs
#     duplicates = combined_df[combined_df.duplicated(subset=image_id_column, keep=False)]
    
#     # Print the duplicate imageIDs
#     if not duplicates.empty:
#         print("Duplicated imageIDs found:")
#         print(duplicates[image_id_column].unique())
#         print(f"Number of duplicated imageIDs: {len(duplicates[image_id_column].unique())}")
#     else:
#         print("No duplicate imageIDs found.")
    
#     # Remove duplicates, keeping only the first occurrence
#     combined_df_unique = combined_df.drop_duplicates(subset=image_id_column, keep='first')
    
#     # Save the combined DataFrame to a new CSV
#     combined_df_unique.to_csv(output_csv, index=False)
#     print(f"Combined CSV saved to {output_csv}")

# # Example usage
# training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\UpdatedTrainingDatasetAttributes.csv'
# testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TestingAttributes.csv'
# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\noDuplicated.csv'

# combine_csv(training_csv, testing_csv, output_csv, image_id_column='Image ID')


# import pandas as pd
# import shutil
# import os

# def copy_images_from_non_duplicated(non_duplicated_csv, image_folder='path_to_images', output_image_folder='path_to_output_images', image_id_column='Image ID'):
#     # Load the non-duplicated attributes CSV
#     non_duplicated_df = pd.read_csv(non_duplicated_csv)
    
#     # Check if the imageID column exists
#     if image_id_column not in non_duplicated_df.columns:
#         print(f"Column '{image_id_column}' not found in the CSV.")
#         return
    
#     # Get the Image IDs from the non-duplicated DataFrame
#     non_duplicated_ids = set(non_duplicated_df[image_id_column])
    
#     # Ensure the output image folder exists
#     if not os.path.exists(output_image_folder):
#         os.makedirs(output_image_folder)
    
#     # Copy images
#     for image_id in non_duplicated_ids:
#         image_filename = f"{image_id}.jpg"
#         source_path = os.path.join(image_folder, image_filename)
#         dest_path = os.path.join(output_image_folder, image_filename)
        
#         if os.path.isfile(source_path):
#             shutil.copy(source_path, dest_path)
#             print(f"Copied {image_filename} to {output_image_folder}")
#         else:
#             print(f"Image {image_filename} not found in {image_folder}")

# # Example usage
# non_duplicated_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\NonDuplicatedFromTestingAttributes.csv'
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TestingDataset'
# output_image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\NonDuplicatedImages'

# copy_images_from_non_duplicated(non_duplicated_csv, image_folder=image_folder, output_image_folder=output_image_folder)



# import pandas as pd

# def find_non_duplicated_from_testing(training_csv, testing_csv, image_id_column='Image ID'):
#     # Load the CSV files
#     training_df = pd.read_csv(training_csv)
#     testing_df = pd.read_csv(testing_csv)
    
#     # Check if the imageID column exists in both CSVs
#     if image_id_column not in training_df.columns or image_id_column not in testing_df.columns:
#         print(f"Column '{image_id_column}' not found in one or both CSVs.")
#         return
    
#     # Get the Image IDs from both DataFrames
#     training_ids = set(training_df[image_id_column])
#     testing_ids = set(testing_df[image_id_column])
    
#     # Find Image IDs present in testing but not in training
#     non_duplicated_ids = testing_ids - training_ids
    
#     if non_duplicated_ids:
#         print("Non-duplicated Image IDs from testing attributes found:")
        
#         # Filter the testing DataFrame to get rows with non-duplicated Image IDs
#         non_duplicated_df = testing_df[testing_df[image_id_column].isin(non_duplicated_ids)]
        
#         # Print and save the non-duplicated attributes
#         print(f"Total number of non-duplicated Image IDs from testing attributes: {len(non_duplicated_df)}")
        
#         # Save the non-duplicated attributes to a CSV
#         non_duplicated_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\NonDuplicatedFromTestingAttributes.csv'
#         non_duplicated_df.to_csv(non_duplicated_csv, index=False)
#         print(f"Non-duplicated attributes saved to {non_duplicated_csv}")
#     else:
#         print("No non-duplicated Image IDs from testing attributes found.")

# # Example usage
# training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\UpdatedTrainingDatasetAttributes.csv'
# testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TestingAttributes.csv'

# find_non_duplicated_from_testing(training_csv, testing_csv, image_id_column='Image ID')










#Filter the adult images
# import pandas as pd
# import os
# import shutil
# import random
# from PIL import Image

# # Function to filter and copy adult images based on the age range
# def filter_and_copy_adult_images(input_csv, image_folder, output_folder, output_csv, age_column='Age', image_id_column='Image ID', min_age=15, max_age=60, num_samples=300):
#     # Load the CSV file
#     df = pd.read_csv(input_csv)
    
#     # Function to extract the lower and upper age boundaries from the 'Age' column
#     def extract_age_range(age_range_str):
#         try:
#             # Remove 'Age ' prefix and split the range by '-'
#             age_range_str = age_range_str.replace('Age ', '')
#             age_range = age_range_str.split('-')
#             # Convert the lower and upper bounds to integers
#             lower_age = int(age_range[0])
#             upper_age = int(age_range[1]) if len(age_range) > 1 else lower_age  # Handle cases with only one value
#             return lower_age, upper_age
#         except (ValueError, AttributeError):
#             return float('nan'), float('nan')
    
#     # Apply the function to extract min and max age for each row
#     df['min_age'], df['max_age'] = zip(*df[age_column].apply(extract_age_range))
    
#     # Filter rows where min_age >= 15 and max_age <= 60
#     adult_df = df[(df['min_age'] >= min_age) & (df['max_age'] <= max_age)].dropna(subset=['min_age', 'max_age'])
    
#     # Check if there are enough adult samples
#     if len(adult_df) < num_samples:
#         print(f"Warning: Only {len(adult_df)} adult images available, less than the requested {num_samples}.")
#         num_samples = len(adult_df)
    
#     # Randomly select the required number of adult images
#     sampled_adult_df = adult_df.sample(n=num_samples, random_state=42)
    
#     # Save the sampled attributes to a new CSV
#     sampled_adult_df.to_csv(output_csv, index=False)
#     print(f"Sampled adult attributes saved to {output_csv}")
    
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # Copy the corresponding images to the output folder
#     for image_id in sampled_adult_df[image_id_column]:
#         image_path_jpg = os.path.join(image_folder, f"{image_id}.jpg")
#         image_path_png = os.path.join(image_folder, f"{image_id}.png")
        
#         if os.path.exists(image_path_jpg):
#             shutil.copy(image_path_jpg, output_folder)
#         elif os.path.exists(image_path_png):
#             # Convert PNG to JPG and save to output folder
#             image = Image.open(image_path_png).convert('RGB')
#             output_jpg_path = os.path.join(output_folder, f"{image_id}.jpg")
#             image.save(output_jpg_path, "JPEG")
#         else:
#             print(f"Image for ID {image_id} not found.")
    
#     print(f"{num_samples} adult images copied to {output_folder}")

# # Example usage
# input_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10290TrainingDatasetAttributes.csv'
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TrainingDataset'
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\300Adult'
# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\300Adult.csv'

# filter_and_copy_adult_images(input_csv, image_folder, output_folder, output_csv)

    
# import pandas as pd

# def check_duplicates(csv_file, image_id_column='Image ID'):
#     # Load the CSV file
#     df = pd.read_csv(csv_file)
    
#     # Check if the imageID column exists
#     if image_id_column not in df.columns:
#         print(f"Column '{image_id_column}' not found in the CSV.")
#         return
    
#     # Find duplicate imageIDs
#     duplicates = df[df.duplicated(subset=image_id_column, keep=False)]
    
#     # Print the duplicate imageIDs
#     if not duplicates.empty:
#         print("Duplicated Image IDs found:")
#         print(duplicates[image_id_column].unique())
#         print(f"Number of duplicated Image IDs: {len(duplicates[image_id_column].unique())}")
#     else:
#         print("No duplicate Image IDs found.")

# # Example usage
# training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10452TrainingDatasetAttributes.csv'
# check_duplicates(training_csv)






#backup
# import os
# import pandas as pd
# from PIL import Image
# import shutil

# def convert_and_copy_images(training_csv, testing_csv, image_folder, output_folder, output_csv, image_id_column='Image ID'):
#     # Load the CSV files
#     training_df = pd.read_csv(training_csv)
#     testing_df = pd.read_csv(testing_csv)
    
#     # Check if the imageID column exists in both CSVs
#     if image_id_column not in training_df.columns or image_id_column not in testing_df.columns:
#         print(f"Column '{image_id_column}' not found in one or both CSVs.")
#         return
    
#     # Merge both DataFrames on the Image ID column
#     combined_df = pd.concat([training_df, testing_df], ignore_index=True)
    
#     # Remove duplicates, keeping only the first occurrence
#     combined_df_unique = combined_df.drop_duplicates(subset=image_id_column, keep='first')
    
#     # Save the combined DataFrame to a new CSV
#     combined_df_unique.to_csv(output_csv, index=False)
#     print(f"Combined CSV saved to {output_csv}")
    
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # Iterate through unique Image IDs and process corresponding images
#     for image_id in combined_df_unique[image_id_column]:
#         # Check both .jpg and .png formats
#         image_paths = [os.path.join(image_folder, f"{image_id}.jpg"), 
#                        os.path.join(image_folder, f"{image_id}.png")]
        
#         for image_path in image_paths:
#             if os.path.exists(image_path):
#                 # Convert .png to .jpg if necessary
#                 if image_path.lower().endswith('.png'):
#                     with Image.open(image_path) as img:
#                         jpg_path = os.path.join(output_folder, f"{image_id}.jpg")
#                         img.convert('RGB').save(jpg_path, 'JPEG')
#                 else:
#                     # Copy .jpg files directly
#                     shutil.copy(image_path, output_folder)
#                 break  # Stop searching once we find and process the image
#         else:
#             print(f"Image file for ID {image_id} not found in either format.")
    
#     print(f"Images processed and saved to {output_folder}")

# # Example usage
# training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TrainingDatasetAttributes.csv'
# testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TestingAttributes.csv'
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TestingDataset'
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\NonDuplicatedImages'
# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\ss_output.csv'

# convert_and_copy_images(training_csv, testing_csv, image_folder, output_folder, output_csv)






# Second step : check duplicated and combined the testing one into the 8413 image folder, with all the attributes
# import pandas as pd
# import os

# # Function to append '.jpg' extension to imageIDs and save to a folder
# def save_images_from_csv(csv_file, output_folder, image_id_column='Image ID'):
#     # Load the CSV file
#     df = pd.read_csv(csv_file)
    
#     # Ensure the output folder exists, create it if it doesn't
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # Loop through each imageID in the CSV and add '.jpg' extension
#     for image_id in df[image_id_column]:
#         # Create the image filename with .jpg extension
#         image_filename = f"{image_id}.jpg"
        
#         # Path to save the image (dummy empty files in this case)
#         image_path = os.path.join(output_folder, image_filename)
        
#         # Create an empty file for demonstration purposes
#         with open(image_path, 'w') as f:
#             pass  # In real scenarios, you'd save the actual image data here

#         print(f"Saved {image_filename} to {output_folder}")
    
#     print(f"All images saved to {output_folder}")

# # Example usage
# csv_file = r'C:\Users\Huawei\Documents\caiting\FootfallCam\output.csv'  # Combined CSV file path
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\output_images'  # Folder to save the .jpg files

# save_images_from_csv(csv_file, output_folder, image_id_column='Image ID')

# Third step : Add the 1079, check duplicated and add into the output.csv

# import pandas as pd

# # Function to check for duplicates and combine CSV files
# def combine_multiple_csvs(main_csv, csv_1, csv_2, output_csv, image_id_column='Image ID'):
#     # Load the CSV files
#     main_df = pd.read_csv(main_csv)  # This is the previously combined output.csv
#     df_1 = pd.read_csv(csv_1)  # 433 image.csv
#     df_2 = pd.read_csv(csv_2)  # 14 image.csv
    
#     # Combine both new CSVs (433 and 14) into one DataFrame
#     combined_new_df = pd.concat([df_1, df_2], ignore_index=True)
    
#     # Find duplicates within the new combined CSV
#     duplicates = combined_new_df[combined_new_df.duplicated(subset=image_id_column, keep=False)]
#     duplicate_ids = duplicates[image_id_column].unique()

#     # Print out duplicated Image IDs
#     if duplicate_ids.size > 0:
#         print(f"Duplicated imageIDs found in the new files: {duplicate_ids}")
#         print(f"Number of duplicated imageIDs in new files: {len(duplicate_ids)}")
#     else:
#         print("No duplicate imageIDs found in the new files.")
    
#     # Combine the previously output CSV (main_df) with the new combined DataFrame
#     final_combined_df = pd.concat([main_df, combined_new_df], ignore_index=True)
    
#     # Remove duplicates, keeping only the first occurrence of each Image ID
#     final_combined_df_unique = final_combined_df.drop_duplicates(subset=image_id_column, keep='first')
    
#     # Save the final combined DataFrame to a new output CSV
#     final_combined_df_unique.to_csv(output_csv, index=False)
#     print(f"Final combined CSV saved to {output_csv}")

# # Example usage
# main_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\UpdatedTrainingDatasetAttributes.csv'  # The previous output.csv
# csv_1 = r'C:\Users\Huawei\Documents\caiting\FootfallCam\433 FlippedImages.csv'  # 433 image.csv
# csv_2 = r'C:\Users\Huawei\Documents\caiting\FootfallCam\213 Child Testing Dataset.csv'   # 213 image.csv
# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\final_output.csv'  # Final combined output CSV

# combine_multiple_csvs(main_csv, csv_1, csv_2, output_csv, image_id_column='Image ID')





# Fourth step : take 433 image into a folder

# import pandas as pd
# import os
# import shutil

# def copy_images_based_on_csv(csv_file, source_folder, dest_folder, image_extension='.jpg'):
#     """
#     Copy .jpg files based on Image IDs from a CSV file to a destination folder.

#     Args:
#     - csv_file (str): Path to the CSV file containing Image IDs.
#     - source_folder (str): Directory where the source images are located.
#     - dest_folder (str): Directory where the matched images will be copied.
#     - image_extension (str): Extension of the image files (default is '.jpg').

#     Returns:
#     - None
#     """
#     # Read the CSV file containing Image IDs
#     df = pd.read_csv(csv_file)

#     if 'Image ID' not in df.columns:
#         print("CSV file does not contain 'Image ID' column.")
#         return

#     # Ensure destination folder exists
#     if not os.path.exists(dest_folder):
#         os.makedirs(dest_folder)

#     # Get list of .jpg files in the source folder
#     image_files = [f for f in os.listdir(source_folder) if f.endswith(image_extension)]

#     # Set to hold Image IDs for quick lookup
#     image_ids = set(df['Image ID'].astype(str) + image_extension)

#     # Copy matching files to the destination folder
#     for img_file in image_files:
#         if img_file in image_ids:
#             source_path = os.path.join(source_folder, img_file)
#             dest_path = os.path.join(dest_folder, img_file)
#             shutil.copy2(source_path, dest_path)  # Copy file to destination folder

#     print(f"Images have been copied to {dest_folder}")

# # Example usage
# csv_file = r'C:\Users\Huawei\Documents\caiting\FootfallCam\433 image.csv'
# source_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\3030F93E9272 2396Images'
# dest_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\433_images'

# copy_images_based_on_csv(csv_file, source_folder, dest_folder)



# # Example usage
# csv_file = r'C:\Users\Huawei\Documents\caiting\FootfallCam\433 image.csv'  # Path to the CSV file
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\output_images'  # Folder to save the .jpg files

# save_images_from_csv(csv_file, output_folder, image_id_column='Image ID')


# Fifth step : flip the images and save to a new folder and CSV file
# from PIL import Image
# import os
# import pandas as pd
# import csv

# def flip_images_and_rename(input_dir, input_csv, csv_path):
#     output_folder = os.path.join(input_dir, "combined_images")
#     i = 1
#     while os.path.exists(output_folder):
#         output_folder = os.path.join(input_dir, "combined_images" + str(i))
#         i += 1
    
#     os.makedirs(output_folder)

#     # Get list of image files in the input directory
#     image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

#     # Read CSV data containing image attributes
#     csv_data = pd.read_csv(input_csv, header=None)

#     if csv_path == 'FlippedImages.csv':
#         csv_path = os.path.join(output_folder, csv_path)

#     # Open the CSV file for writing the flipped image names and attributes
#     with open(csv_path, mode='w', newline='') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerow(['Image ID', 'Gender', 'Age', 'Emotion'])

#         # Iterate through each row in the CSV data
#         for _, row in csv_data.iterrows():
#             image_name_no_ext = row[0]  # Assuming image names in CSV don't have file extensions

#             # Find the image file with the corresponding name (with any extension)
#             for img in image_files:
#                 if img.startswith(image_name_no_ext):
#                     base_name, ext = os.path.splitext(img)
                    
#                     # Save the original image
#                     original_image_path = os.path.join(input_dir, img)
#                     original_output_path = os.path.join(output_folder, img)
#                     os.rename(original_image_path, original_output_path)  # Move the original image to the output folder

#                     # Flip the image and save it with 'f' appended to the filename
#                     flipped_name = f"{base_name}f{ext}"  # Append 'f' before the extension
#                     flipped_output_path = os.path.join(output_folder, flipped_name)

#                     try:
#                         # Open the original image, flip horizontally, and save to the output directory
#                         image = Image.open(original_output_path).convert('RGB')
#                         flipped_img = image.transpose(Image.FLIP_LEFT_RIGHT)
#                         flipped_img.save(flipped_output_path)

#                         # Extract and map gender, age, and emotion from the CSV row
#                         gender = row[1]
#                         age = row[2]
#                         emotion = row[3]

#                         # Write the original and flipped image names and attributes to the CSV file
#                         csv_writer.writerow([img, gender, age, emotion])  # Original image
#                         csv_writer.writerow([flipped_name, gender, age, emotion])  # Flipped image
#                     except Exception as e:
#                         print(f"Error processing image {img}: {e}")
#                     break  # Stop searching for the image once found

#     print('Successfully flipped the images and saved to CSV.')
#     print(f'Combined Output folder::\n{output_folder}')
#     print(f'CSV file created at::\n{csv_path}')

# def main():
#     # Hardcoded paths for input folder and CSV files
#     input_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\output_images'  # Replace with the actual image folder path
#     input_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\433 image.csv'  # Replace with the actual CSV file path
#     output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\433 FlippedImages.csv'  # Output CSV file path

#     # Call the function to flip images and save to CSV
#     flip_images_and_rename(input_folder, input_csv, output_csv)

# if __name__ == "__main__":
#     main()



# Fifth step : flip the images and save to a new folder and CSV file
# from PIL import Image
# import os
# import pandas as pd
# import csv
# import shutil  # Use shutil for copying files instead of moving

# def flip_images_and_rename(input_dir, input_csv, csv_path):
#     # Create a new folder for combined (original + flipped) images
#     output_folder = os.path.join(input_dir, "combined_images")
#     i = 1
#     while os.path.exists(output_folder):
#         output_folder = os.path.join(input_dir, "combined_images" + str(i))
#         i += 1
    
#     os.makedirs(output_folder)

#     # Get list of image files in the input directory
#     image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

#     # Read CSV data containing image attributes
#     csv_data = pd.read_csv(input_csv)  # Removed header=None

#     # Set the output CSV path correctly inside the output folder if not already specified
#     if csv_path == 'FlippedImages.csv':
#         csv_path = os.path.join(output_folder, csv_path)

#     # Open the CSV file for writing the flipped image names and attributes
#     with open(csv_path, mode='w', newline='') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerow(['Image ID', 'Gender', 'Age', 'Emotion'])

#         # Iterate through each row in the CSV data
#         for _, row in csv_data.iterrows():
#             image_id = row['Image ID']  # Assuming 'Image ID' is the correct column name
#             image_name_no_ext = os.path.splitext(image_id)[0]  # Remove extension for matching

#             # Find the image file with the corresponding name (with any extension)
#             for img in image_files:
#                 if img.startswith(image_name_no_ext):
#                     base_name, ext = os.path.splitext(img)
                    
#                     # Save the original image
#                     original_image_path = os.path.join(input_dir, img)
#                     original_output_path = os.path.join(output_folder, img)
#                     shutil.copy(original_image_path, original_output_path)  # Copy the original image to the output folder

#                     # Flip the image and save it with 'f' appended to the filename
#                     flipped_name = f"{base_name}f{ext}"  # Append 'f' before the extension
#                     flipped_output_path = os.path.join(output_folder, flipped_name)

#                     try:
#                         # Open the original image, flip horizontally, and save to the output directory
#                         image = Image.open(original_output_path).convert('RGB')
#                         flipped_img = image.transpose(Image.FLIP_LEFT_RIGHT)
#                         flipped_img.save(flipped_output_path)

#                         # Extract and map gender, age, and emotion from the CSV row
#                         gender = row['Gender']
#                         age = row['Age']
#                         emotion = row['Emotion']

#                         # Write the original and flipped image names and attributes to the CSV file
#                         csv_writer.writerow([img, gender, age, emotion])  # Original image
#                         csv_writer.writerow([flipped_name, gender, age, emotion])  # Flipped image
#                     except Exception as e:
#                         print(f"Error processing image {img}: {e}")
#                     break  # Stop searching for the image once found

#     print('Successfully flipped the images and saved to CSV.')
#     print(f'Combined Output folder::\n{output_folder}')
#     print(f'CSV file created at::\n{csv_path}')

# def main():
#     # Hardcoded paths for input folder and CSV files
#     input_folder = r'C:\Users\Meta\Desktop\FaceCam Project\MontVR\3030F93E9272-Aug-Image'  # Replace with the actual image folder path
#     input_csv = r'C:\Users\Meta\Desktop\FaceCam Project\MontVR\Facecam Project - 3030F93E9272 Aug Annotated.csv'  # Replace with the actual CSV file path
#     output_csv = r'C:\Users\Meta\Desktop\FaceCam Project\MontVR\3030F93E9272 Aug Annotated_FlippedImages.csv'  # Output CSV file path

#     # Call the function to flip images and save to CSV
#     flip_images_and_rename(input_folder, input_csv, output_csv)

# if __name__ == "__main__":
#     main()

import pandas as pd

def count_complete_rows(input_csv):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Check for rows where all columns ('Image ID', 'Gender', 'Age', 'Emotion') have values
    complete_rows = df.dropna(subset=['Image ID', 'Gender', 'Age', 'Emotion'])

    # Count the number of complete rows
    num_complete_rows = len(complete_rows)

    # Print the count of complete rows
    print(f"Number of rows with complete data: {num_complete_rows}")
    return num_complete_rows

# Example usage
input_csv = r'C:\Users\Meta\Desktop\FaceCam Project\MontVR\Facecam Project - 3030F93E9272 July Annotated.csv'
count_complete_rows(input_csv)



#Get the new attributes and image from the ffc link
# import pandas as pd
# import requests
# import os

# def download_images_and_update_csv(attributes_csv, output_csv, image_folder):
#     # Step 1: Load the CSV file
#     attributes_df = pd.read_csv(attributes_csv)

#     # Step 2: Create the output image folder if it doesn't exist
#     if not os.path.exists(image_folder):
#         os.makedirs(image_folder)

#     # Step 3: Iterate over the DataFrame and download each image
#     for index, row in attributes_df.iterrows():
#         image_id = row['Image ID']
#         image_url = row['Link']

#         # Download the image
#         image_extension = image_url.split('.')[-1]  # Get the file extension (jpg or png)
#         image_path = os.path.join(image_folder, f"{image_id}.{image_extension}")

#         try:
#             response = requests.get(image_url, stream=True)
#             if response.status_code == 200:
#                 with open(image_path, 'wb') as img_file:
#                     img_file.write(response.content)
#                 print(f"Downloaded: {image_path}")
#             else:
#                 print(f"Failed to download image: {image_url}")
#         except Exception as e:
#             print(f"Error occurred while downloading {image_url}: {e}")

#     # Step 4: Drop the 'Link' column
#     attributes_df.drop(columns=['Link'], inplace=True)

#     # Step 5: Save the updated DataFrame to a new CSV file
#     attributes_df.to_csv(output_csv, index=False)
#     print(f"Updated attributes CSV saved to {output_csv}")

# # Example usage
# attributes_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\Facecam Project - Copy of 3030F93E9272 Annotated (24_9).csv'  # Replace with your actual path to the CSV
# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\NewDataset.csv'  # Path to save the updated CSV
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\NewDataset'  # Path to save the downloaded images

# download_images_and_update_csv(attributes_csv, output_csv, image_folder)
 
# Sixth step : get the 400 images from the annotated dataset and save to a folder

# import pandas as pd
# import requests
# import os

# def download_images_from_csv(csv_file, image_folder):
#     # Create the image folder if it doesn't exist
#     if not os.path.exists(image_folder):
#         os.makedirs(image_folder)

#     # Read the CSV file
#     data = pd.read_csv(csv_file)

#     # Iterate over each row in the CSV
#     for _, row in data.iterrows():
#         image_id = row['ImageID']  # Assuming the Image ID column is named 'Image ID'
#         image_url = row['Link']     # Assuming the Link column is named 'Link'
        
#         try:
#             # Send a request to download the image
#             response = requests.get(image_url)
#             response.raise_for_status()  # Check for any errors

#             # Save the image with the Image ID as the filename
#             image_path = os.path.join(image_folder, f"{image_id}.jpg")
#             with open(image_path, 'wb') as file:
#                 file.write(response.content)

#             print(f"Downloaded {image_id}.jpg")
        
#         except Exception as e:
#             print(f"Failed to download {image_url}: {e}")

# # Define file paths
# csv_file_path = r'C:\Users\Huawei\Documents\caiting\FootfallCam\Relaxo image.csv'  # Update with your CSV file path
# output_image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\Relaxo image'  # Folder where images will be saved

# # Call the function
# download_images_from_csv(csv_file_path, output_image_folder)


# Step 7 : Combined two csv File

# import pandas as pd

# def concatenate_csv_files(file1, file2, output_file):
#     # Read both CSV files into pandas DataFrames
#     csv1 = pd.read_csv(file1)
#     csv2 = pd.read_csv(file2)

#     # Concatenate the two DataFrames
#     combined_data = pd.concat([csv1, csv2], ignore_index=True)

#     # Save the combined DataFrame to a new CSV file
#     combined_data.to_csv(output_file, index=False)

#     print(f"Combined CSV file saved to {output_file}")

# # File paths
# csv_file1 = r'C:\Users\Huawei\Documents\caiting\FootfallCam\final_output.csv'  # Replace with the actual path of your first CSV
# csv_file2 = r'C:\Users\Huawei\Documents\caiting\FootfallCam\800 Flipped images.csv'  # Replace with the actual path of your second CSV
# output_csv_file = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10452TrainingDatasetAttributes.csv'  # Replace with the output path for the combined CSV

# # Call the function
# concatenate_csv_files(csv_file1, csv_file2, output_csv_file)


# import pandas as pd
# import os

# def compare_image_ids(training_csv, image_folder):
#     # Load the CSV file with training dataset attributes
#     training_df = pd.read_csv(training_csv)
    
#     # Check if 'Image ID' column exists in the CSV
#     if 'Image ID' not in training_df.columns:
#         print("Column 'Image ID' not found in the CSV.")
#         return
    
#     # Get the list of Image IDs from the training CSV
#     csv_image_ids = training_df['Image ID'].astype(str).tolist()
    
#     # Get the list of Image IDs from the image folder (excluding file extensions)
#     image_ids_in_folder = []
#     for filename in os.listdir(image_folder):
#         base_name, ext = os.path.splitext(filename)
#         if ext.lower() in ['.jpg', '.png']:
#             image_ids_in_folder.append(base_name)
    
#     # Find Image IDs that are in the folder but not in the CSV
#     missing_in_csv = [img_id for img_id in image_ids_in_folder if img_id not in csv_image_ids]
    
#     # Print out the results
#     if missing_in_csv:
#         print("Image IDs in the folder but not in the CSV:")
#         print(missing_in_csv)
#         print(f"Number of missing Image IDs: {len(missing_in_csv)}")
#     else:
#         print("All Image IDs in the folder are present in the CSV.")

# # Example usage
# training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10452TrainingDatasetAttributes.csv'
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TrainingDataset'

# compare_image_ids(training_csv, image_folder)


# import pandas as pd
# import os
# import shutil

# def find_and_copy_duplicates(csv_file, image_folder, output_folder, image_id_column='Image ID'):
#     # Load the CSV file
#     df = pd.read_csv(csv_file)
    
#     # Check if the imageID column exists
#     if image_id_column not in df.columns:
#         print(f"Column '{image_id_column}' not found in the CSV.")
#         return
    
#     # Get the list of Image IDs from the CSV
#     image_ids_from_csv = set(df[image_id_column].astype(str).tolist())
    
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # List all image files in the image folder
#     image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png'))]
    
#     # Find duplicates
#     duplicates = [f for f in image_files if os.path.splitext(f)[0] in image_ids_from_csv]
    
#     if duplicates:
#         print(f"Found {len(duplicates)} duplicated images.")
#         # Copy duplicated images to the output folder
#         for image in duplicates:
#             shutil.copy(os.path.join(image_folder, image), os.path.join(output_folder, image))
#         print(f"Copied {len(duplicates)} duplicated images to {output_folder}.")
#     else:
#         print("No duplicated images found.")

# # Example usage
# csv_file = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10290TrainingDatasetAttributes.csv'  # CSV file with Image IDs
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TrainingDataset'  # Folder with images
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\ng'  # Folder to save duplicated images

# find_and_copy_duplicates(csv_file, image_folder, output_folder)


# import pandas as pd
# import os

# def update_training_dataset(csv_file, image_folder, output_csv, image_id_column='Image ID'):
#     # Load the CSV file
#     df = pd.read_csv(csv_file)
    
#     # Check if the imageID column exists
#     if image_id_column not in df.columns:
#         print(f"Column '{image_id_column}' not found in the CSV.")
#         return
    
#     # Get the list of Image IDs from the CSV
#     image_ids_from_csv = set(df[image_id_column].astype(str).tolist())
    
#     # List all image files in the image folder
#     image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png'))]
    
#     # Get the set of IDs that are in the image folder
#     image_ids_from_folder = set(os.path.splitext(f)[0] for f in image_files)
    
#     # Find duplicated Image IDs (present in both the CSV and the folder)
#     duplicated_image_ids = image_ids_from_csv.intersection(image_ids_from_folder)
    
#     # Filter the DataFrame to keep only the rows with duplicated Image IDs
#     filtered_df = df[df[image_id_column].astype(str).isin(duplicated_image_ids)]
    
#     # Save the filtered DataFrame to a new CSV
#     filtered_df.to_csv(output_csv, index=False)
#     print(f"Filtered CSV saved to {output_csv}")

# # Example usage
# csv_file = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TrainingDatasetAttributes.csv'  # Original CSV file
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TrainingDataset'  # Folder with images
# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\UpdatedTrainingDatasetAttributes.csv'  # New CSV file

# update_training_dataset(csv_file, image_folder, output_csv)



#Final step
# import pandas as pd

# def combine_csv_files(csv_files, output_csv):
#     # List to hold DataFrames
#     dfs = []
    
#     # Read each CSV file into a DataFrame and append to the list
#     for csv_file in csv_files:
#         df = pd.read_csv(csv_file)
#         dfs.append(df)
    
#     # Concatenate all DataFrames
#     combined_df = pd.concat(dfs, ignore_index=True)
    
#     # Save the combined DataFrame to a new CSV
#     combined_df.to_csv(output_csv, index=False)
#     print(f"Combined CSV saved to {output_csv}")

# # List of CSV files to combine
# csv_files = [
#     r'C:\Users\Huawei\Documents\caiting\FootfallCam\800 Flipped images.csv',
#     r'C:\Users\Huawei\Documents\caiting\FootfallCam\213 Child Testing Dataset.csv',
#     r'C:\Users\Huawei\Documents\caiting\FootfallCam\433 Flipped images.csv',
#     r'C:\Users\Huawei\Documents\caiting\FootfallCam\UpdatedTrainingDatasetAttributes.csv'
# ]

# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\CombinedOutput.csv'

# combine_csv_files(csv_files, output_csv)


# Delete duplicated from adult testing set and get a new training attributes and testing attributes
# import pandas as pd

# def remove_duplicates_between_datasets(training_csv, testing_csv, image_id_column='Image ID'):
#     # Load the CSV files
#     training_df = pd.read_csv(training_csv)
#     testing_df = pd.read_csv(testing_csv)
    
#     # Check if the imageID column exists in both CSVs
#     if image_id_column not in training_df.columns or image_id_column not in testing_df.columns:
#         print(f"Column '{image_id_column}' not found in one or both CSVs.")
#         return
    
#     # Step 1: Remove duplicates within the testing dataset
#     testing_df = testing_df.drop_duplicates(subset=image_id_column)
    
#     # Step 2: Find common Image IDs between the training and testing datasets
#     training_ids = set(training_df[image_id_column])
#     testing_ids = set(testing_df[image_id_column])
    
#     # Find the intersection (duplicates between both datasets)
#     duplicated_ids = training_ids.intersection(testing_ids)
    
#     # Step 3: Remove these duplicates from both DataFrames
#     training_df_cleaned = training_df[~training_df[image_id_column].isin(duplicated_ids)]
#     testing_df_cleaned = testing_df[~testing_df[image_id_column].isin(duplicated_ids)]
    
#     # Step 4: Save the cleaned DataFrames to new CSV files
#     cleaned_training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\FinalCleanedTrainingAttributes.csv'
#     cleaned_testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\FinalCleanedTestingAttributes.csv'
    
#     training_df_cleaned.to_csv(cleaned_training_csv, index=False)
#     testing_df_cleaned.to_csv(cleaned_testing_csv, index=False)
    
#     print(f"Cleaned training attributes saved to {cleaned_training_csv}")
#     print(f"Cleaned testing attributes saved to {cleaned_testing_csv}")

# # Example usage
# training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10290TrainingDatasetAttributes.csv'
# testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TestingAttributes.csv'

# remove_duplicates_between_datasets(training_csv, testing_csv, image_id_column='Image ID')



# Get the image folder as above one
# import os
# import shutil

# def remove_duplicates_between_folders(training_folder, testing_folder, output_training_folder, output_testing_folder):
#     # Ensure the output folders exist, or create them
#     if not os.path.exists(output_training_folder):
#         os.makedirs(output_training_folder)
#     if not os.path.exists(output_testing_folder):
#         os.makedirs(output_testing_folder)
    
#     # Step 1: Get the base names of image files (without extensions) from both folders
#     training_images = {}
#     testing_images = {}

#     # Collect image IDs from the training folder
#     for file_name in os.listdir(training_folder):
#         if file_name.endswith(('.jpg', '.png')):
#             image_id = os.path.splitext(file_name)[0]
#             training_images[image_id] = file_name  # Store full file name (with extension)

#     # Collect image IDs from the testing folder
#     for file_name in os.listdir(testing_folder):
#         if file_name.endswith(('.jpg', '.png')):
#             image_id = os.path.splitext(file_name)[0]
#             testing_images[image_id] = file_name  # Store full file name (with extension)

#     # Step 2: Find the intersection (duplicates) between training and testing image IDs
#     duplicated_ids = set(training_images.keys()).intersection(testing_images.keys())

#     # Step 3: Copy non-duplicated images to output folders
#     # Training images (skip duplicates)
#     for image_id, file_name in training_images.items():
#         if image_id not in duplicated_ids:
#             source_path = os.path.join(training_folder, file_name)
#             dest_path = os.path.join(output_training_folder, file_name)
#             shutil.copy(source_path, dest_path)
#             print(f"Copied {file_name} to {output_training_folder}")
    
#     # Testing images (skip duplicates)
#     for image_id, file_name in testing_images.items():
#         if image_id not in duplicated_ids:
#             source_path = os.path.join(testing_folder, file_name)
#             dest_path = os.path.join(output_testing_folder, file_name)
#             shutil.copy(source_path, dest_path)
#             print(f"Copied {file_name} to {output_testing_folder}")

#     print(f"Duplicates removed. Cleaned images saved to '{output_training_folder}' and '{output_testing_folder}'.")

# # Example usage
# training_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TrainingDataset'
# testing_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\TestingDataset'
# output_training_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\FinalCleanedTrainingImages'
# output_testing_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\FinalCleanedTestingImages'

# remove_duplicates_between_folders(training_folder, testing_folder, output_training_folder, output_testing_folder)

#Choose the adult testing dataset
# import pandas as pd

# def exclude_testing_attributes(training_csv, testing_csv, output_csv, image_id_column='Image ID'):
#     # Step 1: Load the training and testing attributes CSV files
#     training_df = pd.read_csv(training_csv)
#     testing_df = pd.read_csv(testing_csv)
    
#     # Step 2: Get the Image IDs from the testing DataFrame
#     testing_ids = set(testing_df[image_id_column])

#     # Step 3: Remove the testing attributes from the training DataFrame
#     updated_training_df = training_df[~training_df[image_id_column].isin(testing_ids)]
    
#     # Step 4: Save the updated training attributes to a new CSV
#     updated_training_df.to_csv(output_csv, index=False)
#     print(f"Updated training attributes saved to {output_csv}")

# # Example usage
# training_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10148TrainingDatasetAttributes.csv'
# testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\AdultTesting.csv'  # This should point to the CSV with the 300 selected attributes
# output_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\UpdatedTrainingAttributes.csv'

# exclude_testing_attributes(training_csv, testing_csv, output_csv, image_id_column='Image ID')


#Output the testingimage folder
# import os
# import shutil

# def copy_non_duplicated_images(folder1, folder2, output_folder):
#     # Step 1: Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Step 2: Get lists of images in both folders
#     images1 = {file for file in os.listdir(folder1) if file.lower().endswith(('.jpg', '.png'))}
#     images2 = {file for file in os.listdir(folder2) if file.lower().endswith(('.jpg', '.png'))}

#     # Step 3: Find non-duplicated images
#     unique_to_folder1 = images1 - images2
#     unique_to_folder2 = images2 - images1

#     # Step 4: Copy non-duplicated images to the output folder
#     for image in unique_to_folder1:
#         shutil.copy(os.path.join(folder1, image), output_folder)
#         print(f"Copied {image} from Folder 1 to {output_folder}.")

#     for image in unique_to_folder2:
#         shutil.copy(os.path.join(folder2, image), output_folder)
#         print(f"Copied {image} from Folder 2 to {output_folder}.")

#     print(f"Total unique images copied: {len(unique_to_folder1) + len(unique_to_folder2)}")

# # Example usage
# folder1 = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10148TrainingDataset'  # Path to the first image folder
# folder2 = r'C:\Users\Huawei\Documents\caiting\FootfallCam\ImageFolder2'  # Path to the second image folder
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\UniqueImages'  # Path to the output folder

# copy_non_duplicated_images(folder1, folder2, output_folder)

# import os
# import pandas as pd
# import shutil

# def find_and_copy_duplicates(testing_csv, image_folder, output_folder, image_id_column='Image ID'):
#     # Step 1: Load the testing attributes CSV
#     testing_df = pd.read_csv(testing_csv)

#     # Step 2: Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Step 3: Get the Image IDs from the testing DataFrame
#     testing_ids = set(testing_df[image_id_column].tolist())
    
#     # Step 4: Find duplicates in the image folder
#     image_count = {}
    
#     for image_id in testing_ids:
#         for extension in ['.jpg', '.png']:  # Check for both file types
#             image_file = f"{image_id}{extension}"
#             image_path = os.path.join(image_folder, image_file)
#             if os.path.exists(image_path):
#                 if image_file in image_count:
#                     image_count[image_file] += 1
#                 else:
#                     image_count[image_file] = 1

#     # Step 5: Copy duplicates to the output folder
#     for image_file, count in image_count.items():
#         if count > 1:  # Only consider files that appear more than once
#             shutil.copy(os.path.join(image_folder, image_file), output_folder)
#             print(f"Copied duplicate {image_file} to {output_folder}.")

#     print(f"Total duplicates copied: {len([file for file in image_count if image_count[file] > 1])}")

# # Example usage
# testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\9848TrainingDatasetAttributes.csv'  # Path to the testing attributes CSV
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10148TrainingDataset'  # Path to the image folder
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\AdultTestingImages'  # Path for the output folder

# find_and_copy_duplicates(testing_csv, image_folder, output_folder, image_id_column='Image ID')

 #Find the adult testing images
# import os
# import pandas as pd
# import shutil

# def copy_images_based_on_testing_attributes(testing_csv, image_folder, output_image_folder, missing_image_csv, image_id_column='Image ID'):
#     # Step 1: Load the testing attributes CSV
#     testing_df = pd.read_csv(testing_csv)

#     # Step 2: Create the output image folder if it doesn't exist
#     if not os.path.exists(output_image_folder):
#         os.makedirs(output_image_folder)

#     # List to keep track of missing Image IDs
#     missing_image_ids = []

#     # Step 3: Copy corresponding images to the output image folder
#     for image_id in testing_df[image_id_column]:
#         found = False
#         for extension in ['.jpg', '.png']:  # Check both .jpg and .png files
#             image_file = f"{image_id}{extension}"  # Add the extension
#             image_path = os.path.join(image_folder, image_file)
#             if os.path.exists(image_path):
#                 shutil.copy(image_path, output_image_folder)
#                 print(f"Copied {image_file} to {output_image_folder}.")
#                 found = True
#                 break  # Stop after copying the first found image

#         if not found:
#             print(f"Image for {image_id} not found in the image folder.")
#             missing_image_ids.append(image_id)

#     # Step 4: Save the missing Image IDs to a CSV
#     if missing_image_ids:
#         missing_image_df = pd.DataFrame({image_id_column: missing_image_ids})
#         missing_image_df.to_csv(missing_image_csv, index=False)
#         print(f"Missing Image IDs saved to {missing_image_csv}")
#     else:
#         print("All images were found.")

# # Example usage
# testing_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\AdultTesting.csv'  # Path to your testing CSV
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10148TrainingDataset'  # Path to your images
# output_image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\SelectedImages'  # Path to output images
# missing_image_csv = r'C:\Users\Huawei\Documents\caiting\FootfallCam\MissingImages.csv'  # Path for missing images CSV

# copy_images_based_on_testing_attributes(testing_csv, image_folder, output_image_folder, missing_image_csv, image_id_column='Image ID')


#Get the finalised dataset images
# import os
# import shutil

# def update_training_image_folder(training_image_folder, testing_image_folder, output_folder):
#     # Step 1: Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Step 2: Get the list of images in the testing folder
#     testing_images = {file.lower() for file in os.listdir(testing_image_folder) if file.lower().endswith(('.jpg', '.png'))}

#     # Step 3: Copy images from the training folder to the output folder, excluding testing images
#     for file in os.listdir(training_image_folder):
#         if file.lower().endswith(('.jpg', '.png')):
#             if file.lower() not in testing_images:  # Check if the image is not in the testing folder
#                 shutil.copy(os.path.join(training_image_folder, file), output_folder)
#                 print(f"Copied {file} to {output_folder}.")
#             else:
#                 print(f"Skipped {file} (found in testing images).")

#     print("Updated training image folder created.")

# # Example usage
# training_image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10148TrainingDataset'
# testing_image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\SelectedImages'
# output_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\UpdatedTrainingImages'  # Path to output folder

# update_training_image_folder(training_image_folder, testing_image_folder, output_folder)

#Final : Check gpt duplicated images or not

# import os
# from collections import Counter
# import pandas as pd

# # Function to check for duplicate images in the folder
# def find_duplicate_images_in_folder(image_folder):
#     # Step 1: List all image files in the folder
#     image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('.jpg', '.png'))]

#     # Step 2: Count duplicates using Counter
#     duplicate_counts = Counter(image_files)

#     # Step 3: Identify and print duplicates
#     duplicates = {file: count for file, count in duplicate_counts.items() if count > 1}

#     if duplicates:
#         print("Duplicated image files found:")
#         for file, count in duplicates.items():
#             print(f"{file}: {count} times")
#     else:
#         print("No duplicated image files found.")

# # Function to check for duplicate entries in the attributes CSV
# def find_duplicate_entries_in_csv(csv_file, column_name='Image ID'):
#     # Step 1: Load the CSV file
#     df = pd.read_csv(csv_file)

#     # Step 2: Check for duplicates based on the specified column (default: 'Image ID')
#     duplicates = df[df.duplicated(subset=[column_name], keep=False)]  # Keep=False shows all duplicates

#     if not duplicates.empty:
#         print(f"Duplicated rows found in {csv_file} based on '{column_name}':")
#         print(duplicates)
#     else:
#         print(f"No duplicated entries found in {csv_file} based on '{column_name}'.")

# # Example usage for image folder duplication check
# image_folder = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10469TrainingDataset'  # Path to your image folder
# find_duplicate_images_in_folder(image_folder)

# # Example usage for CSV duplication check
# csv_file = r'C:\Users\Huawei\Documents\caiting\FootfallCam\10469TrainingDatasetAttributes.csv'  # Path to your CSV file
# find_duplicate_entries_in_csv(csv_file, column_name='Image ID')  # Check duplicates in 'Image ID' column










