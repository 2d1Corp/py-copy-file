def copy_file(command: str) -> None:
    try:
        cp, file_in, file_out = command.split(" ")
        if cp != "cp":
            raise ValueError()
        if file_in != file_out:
            with (
                open(file_in, "r") as file_in,
                open(file_out, "w") as file_out
            ):
                for line in file_in:
                    file_out.write(line)
    except ValueError:
        pass
    except FileNotFoundError:
        pass
