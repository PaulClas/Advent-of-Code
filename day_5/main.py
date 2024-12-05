def parse_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    sections = content.split('\n\n')
    if len(sections) < 2:
        raise ValueError("The file does not contain the expected two sections.")

    # Parse the first section for page ordering rules
    page_ordering_rules = []
    for line in sections[0].strip().split('\n'):
        if '|' in line:
            x, y = line.split('|')
            page_ordering_rules.append((int(x.strip()), int(y.strip())))

    # Parse the second section for updates
    updates = []
    for line in sections[1].strip().split('\n'):
        updates.append([int(num) for num in line.split(',')])

    return page_ordering_rules, updates

def verify_updates(page_ordering_rules, updates):
    valid_updates = []
    invalid_updates = []
    for update in updates:
        if len(update) % 2 == 0:
            invalid_updates.append(update)
            continue

        is_valid = True
        for x, y in page_ordering_rules:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    is_valid = False
                    break
        if is_valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates

def correct_order(page_ordering_rules, update):
    ordered_update = update[:]
    for x, y in page_ordering_rules:
        if x in ordered_update and y in ordered_update:
            x_index = ordered_update.index(x)
            y_index = ordered_update.index(y)
            if x_index > y_index:
                ordered_update[x_index], ordered_update[y_index] = ordered_update[y_index], ordered_update[x_index]
    return ordered_update

def sum_middle_numbers(updates):
    total_sum = 0
    for update in updates:
        if len(update) % 2 == 1:  # Ensure there is a single middle number
            middle_index = len(update) // 2
            middle_number = update[middle_index]
            print("Middle Number:", middle_number)
            total_sum += middle_number
    return total_sum

if __name__ == "__main__":
    filename = 'input.txt'
    page_ordering_rules, updates = parse_file(filename)
    print("Page Ordering Rules:", page_ordering_rules)
    print("Updates:", updates)

    valid_updates, invalid_updates = verify_updates(page_ordering_rules, updates)
    print("Valid Updates:", valid_updates)
    print("Invalid Updates:", invalid_updates)

    total_sum_valid = sum_middle_numbers(valid_updates)
    print("Sum of all middle numbers in valid updates:", total_sum_valid)

    corrected_invalid_updates = [correct_order(page_ordering_rules, update) for update in invalid_updates]
    print("Corrected Invalid Updates:", corrected_invalid_updates)

    revalidated_valid_updates, revalidated_invalid_updates = verify_updates(page_ordering_rules, corrected_invalid_updates)
    print("Revalidated Valid Updates:", revalidated_valid_updates)
    print("Revalidated Invalid Updates:", revalidated_invalid_updates)

    total_sum_revalidated_valid = sum_middle_numbers(revalidated_valid_updates)
    print("Sum of all middle numbers in revalidated valid updates:", total_sum_revalidated_valid)

    # Correct the revalidated invalid updates until there are none left to revalidate and correct
    while revalidated_invalid_updates:
        re_corrected_invalid_updates = [correct_order(page_ordering_rules, update) for update in revalidated_invalid_updates]
        print("Re-Corrected Invalid Updates:", re_corrected_invalid_updates)

        revalidated_valid_updates, revalidated_invalid_updates = verify_updates(page_ordering_rules, re_corrected_invalid_updates)
        print("Revalidated Valid Updates:", revalidated_valid_updates)
        print("Revalidated Invalid Updates:", revalidated_invalid_updates)

        total_sum_revalidated_valid += sum_middle_numbers(revalidated_valid_updates)

    total_sum_final_valid = sum_middle_numbers(revalidated_valid_updates)
    print("Sum of all middle numbers in final valid updates:", total_sum_final_valid)

    # Add the sum of all middle numbers in final valid updates to the sum of all middle numbers in revalidated valid updates
    total_sum_combined = total_sum_revalidated_valid + total_sum_final_valid
    print("Total sum of all middle numbers in revalidated and final valid updates:", total_sum_combined)