
csv_df.write.mode('overwrite').parquet("s3://vishaldevbucket/outbound/csvoutput/")

job.commit()
