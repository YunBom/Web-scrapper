def save_file(file_name, jobs) :
    file = open(f"{file_name}.csv", "w")
    file.write("Title, Company, Location, URL\n")
    
    for job in jobs:
        file.write(f"{job['title']}, {job['company']}, {job['location']},{job['link']}\n")
    
    file.close()