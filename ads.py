def remove_ads(page):
    H, W = map(int, page[0].split())
    image_chars = set("!?,.")

    # Find the borders of the images
    borders = []
    for i in range(1, H+1):
        if page[i][0] == '+' and page[i][W-1] == '+':
            borders.append(i)
    num_borders = len(borders)

    # Find the boundaries of each image
    image_boundaries = []
    for i in range(num_borders - 1):
        image_boundaries.append((borders[i] + 1, borders[i+1] - 1))
    image_boundaries.append((borders[num_borders - 1] + 1, H))

    # Identify the ads and remove them
    for image_boundary in image_boundaries:
        image_rows = page[image_boundary[0]:image_boundary[1] + 1]
        ad_chars = set()
        for row in image_rows:
            for char in row:
                if char not in image_chars and char != ' ' and char != '+':
                    ad_chars.add(char)

        if len(ad_chars) > 0:
            # Find the smallest image containing the ad characters
            min_area = float('inf')
            min_image_row = -1
            for i, row in enumerate(image_rows):
                ad_count = 0
                for char in row:
                    if char in ad_chars:
                        ad_count += 1
                if ad_count > 0:
                    row_area = ad_count * len(row)
                    if row_area < min_area:
                        min_area = row_area
                        min_image_row = i

            # Remove the ad
            ad_row = image_boundary[0] + min_image_row
            for i in range(ad_row, ad_row + len(ad_chars)):
                page[i] = page[i].replace('+', ' ')
                page[i] = page[i].replace('-', ' ')

    # Print the modified page
    for row in page[1:]:
        print(row, end='')

# Read the input
page = []
while True:
    try:
        row = input()
        page.append(row)
    except EOFError:
        break

# Remove ads and print the modified page
remove_ads(page)
