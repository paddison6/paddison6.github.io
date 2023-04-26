#!/usr/bin/env python3

import html

def main():
    date = ""
    while date == "":
        date = input("Review Date (e.g. 16 April 2023): ")
    date = html.escape(date)

    title = ""
    while title == "":
        title = input("Review Title: ")
    title = html.escape(title)

    review = ""
    while review == "":
        review = input("Review Text: ")
    review = html.escape(review)
    
    picsrc = ""
    while picsrc == "":
        picsrc = input("Picture path (e.g. pics/16april2023-spicychicken.jpeg): ")
    picsrc = html.escape(picsrc)

    shortdesc = ""
    while shortdesc == "":
        shortdesc = (input("Short Description [defaults to Soup Picture] (e.g. Spicy Chicken 16 April 2023): ") or "Soup Picture")
    shortdesc = html.escape(shortdesc)

    score = -1.0
    while score < 0:
        try:
            score = float(input("Review Verdict [defaults to 0] (e.g. 7.5): ") or "0")
        except Exception as e:
            print(f"error while getting the score: {e}")
            continue

    reviewId = ""
    while reviewId == "":
        reviewId = input("Review Identifier for features (e.g., spicychicken): ")

    isGuestReview = (input("Is this a guest review? [default \"no\"]: ") or "no")
    if isGuestReview != "no":
        isGuestReview = "yes"

    reviewerName = "Peter Addison" 
    if isGuestReview == "yes":
        reviewerName = input("Reviewer Name: ")
        while reviewerName == "":
            reviewerName = input("Reviewer Name: ")
    reviewerName = html.escape(reviewerName)

    template_str = ""
    if isGuestReview != "yes":
        with open("reviews/review-template.html") as fin:
            template_str = fin.read()
    else:
        with open("reviews/guest-review-template.html") as fin:
            template_str = fin.read()
    if template_str == "":
        print("Could not read/find the template. Terminating")
        exit()

    template_str = template_str.replace("DATE", f'{date.strip()}')
    if isGuestReview == "yes":
        template_str = template_str.replace("TITLE", f'{title.strip()} by {reviewerName.strip()}')
    else:
        template_str = template_str.replace("TITLE", f'{title.strip()}')
    template_str = template_str.replace("REVIEW", f'{review.strip()}')
    template_str = template_str.replace("SCORE", f'{score:.1f}')
    template_str = template_str.replace("SHORTDESC", f'{shortdesc.strip()}')
    template_str = template_str.replace("PICSRC", f'{picsrc.strip()}')
    template_str = template_str.replace("SHRTDT", f'{date.lower().replace(" ", "").strip()}')
    template_str = template_str.replace("RID", f'{reviewId.lower().replace(" ", "").strip()}')

    news = ""
    fileExportedTo = ""
    if isGuestReview == "yes":
        with open(f'reviews/data/guests/{date.lower().replace(" ", "").strip()}.html', "w+") as fout:
            fout.write(template_str)
            fileExportedTo = f'reviews/data/guests/{date.lower().replace(" ", "").strip()}.html'
    else:
        with open(f'reviews/data/{date.lower().replace(" ", "").strip()}.html', "w+") as fout:
            fout.write(template_str)
            fileExportedTo = f'reviews/data/{date.lower().replace(" ", "").strip()}.html'
    summary = f"""
Summary:
  - Date: {date}
  - Title: {title}
  - Review: {review}
  - Picture Location: {picsrc}
  - Short Description: {shortdesc}
  - Score: {score}/10
  - ReviewID: {reviewId}
  - Is Guest Review: {isGuestReview}
  - Reviewer Name: {reviewerName}
Review is exported to the following path:
  - Path: {fileExportedTo}
"""
    print(summary)
    caveat = """
Also, please check the index.html
in the main folder to add news.

In addition, check the reviews/index.html
and reviews/stats.html
to add news and stats with the correct
hyperlinks.

Finally, run the updated.sh script in the
main folder, and before running it, change the
date to the current date.
"""
    print(caveat)

if (__name__ == "__main__"):
    main()