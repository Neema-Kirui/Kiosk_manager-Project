# Capstone Project: The Kiosk Manager

## The Brief

Every skill you've learned so far — variables, conditionals, loops, functions, lists/dicts/tuples/sets, and string/file handling — goes into ONE real program.

**The scenario:** your group has been hired to build a management system for a small Nairobi kiosk. 
The owner needs to track stock, record sales, and keep everything saved between days — right now they're doing it all in a notebook.

This is deliberately open-ended. There is no single correct file structure or exact wording — what matters is that your program actually WORKS, handles messy real input sensibly, and uses the skills below in a genuine way, not just technically present.

---

## What This Project Proves You Can Do

### Skills This Project Must Demonstrate

| Session | How It Shows Up |
|---|---|
| Session 1 – Basics | Clean `input()` prompts, correct data types, f-string formatted output throughout |
| Session 2 – Conditionals | `if/elif/else` driving real business logic (enough stock? valid menu choice? low balance?) |
| Session 3 – Loops | A menu that runs with `while True` until the user exits; `for` loops processing lists of items |
| Session 4 – Functions | Every feature built as its OWN function, called from a clean main flow — not one giant block of code |
| Session 5 – Data Structures | A dictionary for stock, a list for the sales log, a set for unique items sold, at least one tuple |
| Session 6 – Strings & Files | Input cleaned/validated with string methods, and data that SURVIVES between runs using file read/write |

---

## Core Requirements — Build These

### 1. Welcome & Setup

- On startup, ask for the kiosk's name and the owner's name.
- Print a clean, formatted welcome banner using an f-string, e.g. `Welcome to Navas's Kiosk Manager, run by Navas Herbert`.
- Clean any name input with `.strip()` and `.title()` before using it — don't trust raw `input()`.

### 2. Main Menu Loop

- Use a `while True` loop to show a menu and keep running until the user chooses to exit.
- Suggested options: 1) View Stock, 2) Add/Restock a Product, 3) Sell a Product, 4) View Sales Report, 5) Search Products, 6) Exit.
- Validate the menu choice using `.isdigit()` before converting with `int()` — don't let a typo crash the whole program.
- If the choice is invalid or out of range, print a friendly message and show the menu again, don't crash.

### 3. Inventory Management (dictionary)

- Store stock as a dictionary: `{'Bread': {'price': 65, 'quantity': 20}, ...}` — or a similar structure your group agrees on.
- Support viewing the full inventory, formatted neatly (aligned columns using the f-string padding skills from Session 6).
- Support restocking an existing item OR adding a brand new one if it doesn't exist yet.
- Every inventory-changing action should be its own FUNCTION, not inline code in the menu loop.

### 4. Selling a Product

- Ask which product and how many units. Check there's enough stock using a conditional — if not, print a clear message and don't sell anything.
- If there IS enough stock, reduce the quantity, calculate the total price, and record the sale.
- Each sale should be stored as a TUPLE (or similar) in a sales log LIST, e.g. `(item, quantity, total, ...)`.
- Keep a SET of every unique product name sold today — update it every time a sale happens.

### 5. Sales Report

- Loop through the sales log and print every sale, nicely formatted.
- Calculate and print the TOTAL revenue for the session using an accumulator.
- Print how many UNIQUE products were sold today, using your set from Feature 4.
- Identify and print the best-selling product (by quantity or revenue — your group's choice, just be consistent).

### 6. Search Products

- Let the user type part of a product name (not necessarily the whole thing) and find matching items in the inventory.
- Use string methods to make the search forgiving: `.lower()` on both the search term and the product names, and the `in` operator to check for a partial match.
- Print every matching product with its price and quantity, or a clear "No matches found" message.

### 7. Saving and Loading Data (files)

- When the program starts, check if a save file exists. If it does, LOAD the inventory from it instead of starting empty. If not, start with a small default inventory.
- When the user exits (option 6), WRITE the current inventory to a file so it's still there next time the program runs.
- Also save the sales log from this session to a separate file (e.g. append each session's sales, don't overwrite history).
- You may use plain `.txt` files with your own comma-separated format from Session 6 — the `csv` module is NOT required for this project (that comes in Session 7).

---

## Sample Program Flow (Guide, Not a Template to Copy Exactly)

This is ONE way your menu might look and behave — use it to calibrate the STYLE and POLISH expected, not as code to copy word for word.

**File:** `kiosk_manager.py` (example run)

```text
Welcome to Navas's Kiosk Manager, run by Navas Herbert

===== MAIN MENU =====
1. View Stock
2. Add/Restock a Product
3. Sell a Product
4. View Sales Report
5. Search Products
6. Exit
Enter your choice: 3

Which product? Bread
How many units? 5
Sold 5 Bread for KES 325.

===== MAIN MENU =====
Enter your choice: 6
Saving data... Goodbye, Navas!
```

---

## Suggested Focus Areas

| Area | Covers |
|---|---|
| Menu & Flow | Main menu loop, input validation, overall program flow — the "glue" connecting every other feature's functions together |
| Inventory | View stock, restock, add new products — the dictionary logic |
| Sales & Reporting | Selling products + the sales report: stock checks, sales log (list of tuples), the set of unique items, revenue totals |
| Search & Files | Search feature + file saving/loading — string cleaning for search, reading/writing the save files on startup and exit |

---

## More Features You Could Add

Same skill level, just more of it. All of these stay within Sessions 1–6 — no new modules, no `try/except`, no classes. Pick whichever sound fun; none are required.

### Pick Any — Not Required

- **Shopping basket checkout:** let a customer buy SEVERAL different items in one visit before totalling — collect each item into a list as they go, then loop through it to print an itemised receipt and one grand total.
- **Change calculator:** after taking payment, calculate the change owed, then break it down into how many KES 1000 / 500 / 100 / 50 notes and coins to give back, using floor division (`//`) and modulus (`%`).
- **Top-selling leaderboard:** after a session of sales, sort your sales log to show the top 3 best-selling products by quantity or revenue.
- **Restock alert file:** every time the program exits, write out just the names of low-stock items to a separate `alerts.txt`, so the owner has a printable shopping list for the wholesaler.
- **Customer loyalty tracker:** record a customer name with each sale and build a dictionary of `{customer: total_spent}`. At exit, print the top spender.
- **Human-readable daily report:** beyond just saving raw data, write a nicely formatted, padded/aligned text report (like a real receipt or summary sheet) to a separate file — different from the file you reload data from.
- **Bulk restock mode:** let the owner restock MULTIPLE products in one go by entering a comma-separated list (e.g. `Bread,20 Milk,10`) and parsing it with `.split()` into individual updates.
- **Simple PIN check at startup:** a hardcoded PIN (stored as a string) that must be entered correctly, validated with string comparison, before the main menu even appears.

---

## Submission Guidelines

### What to Hand In

Submit ONE folder containing: your main `.py` file, any sample/starting data files, and a short `README.txt`.

Your program should run without crashing on obviously bad input (letters where numbers are expected, empty input, searching for something that doesn't exist) — test this yourselves before submitting.

Come to the next session ready to run your program live and answer questions about ANY part of it.

### Before You Submit — Self-Check

- [ ] Program runs from a fresh start with NO crashes on normal use
- [ ] Typing letters instead of numbers at any menu/input point does NOT crash the program
- [ ] Every feature (view/restock/sell/report/search) is its own function, called from a clean main flow
- [ ] At least one dictionary, one list, one tuple, and one set are genuinely used (not just declared and ignored)
- [ ] All user-facing text input is cleaned with `.strip()` and appropriate case methods before being used or compared
- [ ] Inventory data is saved to a file when the program exits, and correctly LOADED back in on the next run
- [ ] The sales report shows correct totals — test it against numbers you've calculated by hand
