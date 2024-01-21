#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Richard J. Sears'
VERSION = "1.0.0a (2024-01-21)"

"""
Simple python script that utilizes sas3ircu to locate the SAS controllers on your
system and then allows you to select the controller and outputs all drives on that
controller so you can blink or unblink them for location purposes. Makes finding
drives on your system easy!

Used the Rich library to output a nicely formatted table. 

Works on TrueNAS Scale (Linux based) and SAS3IRCU, it might also work with
SAS2IRCU. 
"""



from rich.console import Console
from rich.table import Table
import subprocess
import re
from datetime import datetime

report_time = datetime.now().strftime('%H:%M:%S')
current_date = datetime.today().strftime('%B %d, %Y')

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode(), error.decode()

def parse_controller_info(output):
    pattern = re.compile(r"(\d+)\s+(\w+)\s+(\w+)h\s+(\w+)h\s+(\w+:\w+:\w+:\w+)\s+(\w+)h\s+(\w+)h")
    matches = re.findall(pattern, output)
    return matches


def print_table_header():
    print()
    console = Console()
    table = Table(title=f':seedling:  [bold][green]Welcome to Drive Locator![/][/] :seedling:',title_style='no reverse', show_footer=False, show_header=True, show_lines=False, header_style="bold blue", show_edge=False)
    table.add_column(f'{current_date} @ {report_time}' ,justify="center", width=80)
    console.print(table)
    print()


def print_table(data):
    console = Console()
    table = Table(title=f':input_numbers:  [bold][yellow]Controller Information[/][/] :input_numbers:', title_style='no reverse', show_header=True, show_lines=False, header_style="bold blue")
    table.add_column("Index", style="cyan", justify="center")
    table.add_column("Type", style="cyan", justify="center")
    table.add_column("Vendor ID", style="cyan", justify="center")
    table.add_column("Device ID", style="cyan", justify="center")
    table.add_column("Pci Address", style="cyan", justify="center")
    table.add_column("Ven ID", style="cyan", justify="center")
    table.add_column("Dev ID", style="cyan", justify="center")

    for entry in data:
        table.add_row(*entry)

    console.print(table)


def print_drive_table(data):
    print()
    print()
    print()
    console = Console()
    table = Table(title=f':memo:  [bold][green]Hard Drive Information[/][/] :memo:', title_style='no reverse', show_header=True, show_lines=False, header_style="bold blue")
    table.add_column("Enclosure", style="cyan", justify="center")
    table.add_column("Slot", style="cyan", justify="center")
    table.add_column("Size (in MB)", style="cyan", justify="center")
    table.add_column("Manufacturer", style="cyan", justify="center")
    table.add_column("Model Number", style="cyan", justify="center")
    table.add_column("Serial Number", style="cyan", justify="center")

    for entry in data:
        table.add_row(*entry)

    console.print(table)


def locate_drive(controller_index, enclosure, slot):
    command = f"sudo /usr/local/bin/sas3ircu {controller_index} locate {enclosure}:{slot} on"
    run_command(command)
    print("Drive ID light should be flashing! Please run ./locate_disk.py -locate_off to disable.")


def stop_locate_drive(controller_index, enclosure, slot):
    command = f"sudo /usr/local/bin/sas3ircu {controller_index} locate {enclosure}:{slot} off"
    run_command(command)


if __name__ == "__main__":
    # Run the initial command to get controller information
    sas3ircu_output, _ = run_command("sudo /usr/local/bin/sas3ircu list")
    controller_info = parse_controller_info(sas3ircu_output)

    if not controller_info:
        print("No SAS controllers found.")
    else:
        # Print the controller information only if there is more than one controller
        print_table_header()
        if len(controller_info) > 0:
            print_table(controller_info)

        # Run the command to display specific controller information
        display_command = f"sudo sas3ircu {controller_info[0][0]} display"
        display_output, _ = run_command(display_command)

        # Parse the display output to locate Hard disk devices
        pattern = re.compile(r"Device is a Hard disk[\s\S]+?Enclosure #[\s\S]+?(\d+)[\s\S]+?Slot #[\s\S]+?(\d+)[\s\S]+?Size \(in MB\)\/\(in sectors\)[\s\S]+?(\d+)[\s\S]+?Manufacturer[\s\S]+?(\w+)[\s\S]+?Model Number[\s\S]+?(\w+)[\s\S]+?Serial No[\s\S]+?(\w+)")
        drive_info_matches = re.findall(pattern, display_output)

        # Print the table for Hard disk devices
        print_drive_table(drive_info_matches)

        # Ask the user if they want to locate or stop locating a drive
        action = input("Choose an action: (blink/unblink) ")
        if action == "blink":
            slot_to_locate = input("Enter the slot number to locate: ")
            corresponding_enclosure = next((enclosure for enclosure, slot, *_ in drive_info_matches if slot == slot_to_locate), None)
            if corresponding_enclosure is not None:
                locate_drive(controller_info[0][0], corresponding_enclosure, slot_to_locate)
            else:
                print("Invalid slot number. Exiting.")
        elif action == "unblink":
            slot_to_stop = input("Enter the slot number to stop location blinking: ")
            corresponding_enclosure = next((enclosure for enclosure, slot, *_ in drive_info_matches if slot == slot_to_stop), None)
            if corresponding_enclosure is not None:
                stop_locate_drive(controller_info[0][0], corresponding_enclosure, slot_to_stop)
            else:
                print("Invalid slot number. Exiting.")
        else:
            print("Invalid action. Exiting.")
