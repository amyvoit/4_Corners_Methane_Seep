# 4_Corners_Methane_Seep

## Project Description & Motivation
This project compiles publicly available methane measurement data from a project initiated by the Colorado Oil & Gas Conservation Commission (now known as the ECMC) in the 1990's to measure & document the natural methane seepage from a geologic formation called the Fruitland Formation in the region of southwestern Colorado known as the Four-Corners. It specifically pulls methane flux measurements from pdf reports published to the ECMC website for the monitoring period of 2012-2020. 

The goal of this project was to see if methane flux measurements recorded during the 2012-2020 period could be correlated and therefore predicted by other regional factors affecting the formation, such as annual precipitation rates, or oil and gas production operations. Oil & gas activity was measured in several different ways. Production from the San Juan Basin for oil, gas and produced water was pulled from the respective governing agencies in both Colorado and New Mexico. Further, many O&G operators re-inject water back into various formations through injection wells. The volume injected into these wells can also be pulled from the same agencies that the production data is reported to. Finally, drilling activity was added in as a potential factor using data published by Baker Hughes on regional rig counts.

After the data was injested, cleaned, and analyzed, some simple Random Forest Regressor models were created on both the larger dataset as a whole and on one specific region from which monitoring occurred. These models were both tuned for optimal hyperparameters per the RandomizedSearchCV functionality provided by Scikit-Learn.

## Project Organization
The main file for this project is a Jupyter Notebook: 
  - MethaneSeep.ipynb

The main data files (all .csv) - some of which were slightly pre-processed manually prior to upload - are located in the file titled:
  - data

The extracted pdf methane measurement tables from the reports uploaded to the ECMC website are located in the file titled:
  - pdfs

I created a python program called "pdf_table_extractor.py" to try and extract the tables from the pdf and convert them into a .csv file. Frankly, this only worked for one of the table files. Since the format changed in the pdf files from year to year, I could not find a solid pythonic solution to extract all of these. The easiest way I found was to use the export functionality of Adobe Acrobat Pro (I got a free 7-day trial) and then use some of the column separation funcitonality of Microsoft Excel to create the final data files found in the data folder. That was the worst part of this process.

Finally, any programs I thought I would need are loaded in the requirements.txt file. I did include some mapping libraries that I didn't end up using. After some digging, the methane measurement locations were recorded in state plane units (northing, easting) which requires conversion to standard lat/long in order to map using Folium or some other program. I believe the library pyproj could do this but would require more digging into that process and mapping projections. So I abandoned that idea for the time being.

## Project Conclusions
The data analysis had some surprising takeaways. First, the variance in the overall dataset was not well described by the chosen factors (oil & gas activity or precipitation). Many of the chosen monitoring areas by the original project consultant seem to consistently have extremely low or zero methane flux values. This means the dataset is quite sparse. The generated Random Forest model ended up performing quite well on the test data set even though the training dataset results in both a tuned and untuned version had disappointing RMSE and R2 values. I believe the cause of this is because the model is likely predicting 0 methane flux, which means it's usually correct based on the high number of observations that had 0's.

Luckily, the data was already partitioned into local "areas" and some areas seem to have consistently high or at least elevated readings. To see if the data analysis changed when the dataset just focused on areas with methane activity, I partitioned out a smaller dataset and performed similar analysis. The smaller dataset ended up showing higher Pearson Correlation Coefficient's with some of the chosen variables - although in surprising ways. Methane flux rates seemed to decrease with increasing Produced Water, Natural Gas, and Rig Counts. On the other hand, with increasing oil production, the methane flux rates seemed to increase. Since the regional O&G operators tend to drill different wells depending upon if they are trying to produce natural gas or oil, it may make sense that these are correlated in opposite directions. Finally, in talking to a local geologist who has studied the methane seeps, he mentioned that increased annual precipitation rates may decrease the methane flux values since it may infilitrate the formation and block the methane gas from escaping. I did find that in these separated areas, preciptiation was negatively correlated with methane flux.

With all that being said, building a Random Forest model on a smaller subset of the data focused just on a single area with high variability in methane flux measurements resulted in uninspiring R2 & RMSE values on the testing datasets. Evaluating the feature importances based on this model also showed that very few of the chosen predictors had any importance on the resulting methane flux measurements. 

The above analysis leads me to conclude that the methane being measured in the Fruitland Formation may have other factors influencing its flux other than precipitation or Basin-level oil & gas activity. 
