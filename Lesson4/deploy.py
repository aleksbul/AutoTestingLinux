from sshcheckers import ssh_checkout, upload_files


def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "qqq", "tests/p7zip-full.deb",
                 "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "qqq", "echo 'qqq' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Setting up"))
    res.append(ssh_checkout("0.0.0.0", "user2", "qqq", "echo 'qqq' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)


if deploy():
    print("Deploy is successful")
else:
    print("Deploy error")
