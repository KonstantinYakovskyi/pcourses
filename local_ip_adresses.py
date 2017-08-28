import subprocess


def get_ip_addresses():
    output = subprocess.check_output("ipconfig")

    result = ''

    lines = output.splitlines()
    lines = filter(lambda x: x, lines)

    for line in lines:
        is_ip_address = 'IPv' in line or 'Subnet Mask' in line or 'Default Gateway' in line

        if is_ip_address:
            result = result + line + '\n'

    print result


if __name__ == '__main__':
    exit(get_ip_addresses())
