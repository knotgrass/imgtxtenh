from subprocess import Popen, PIPE
import os.path


imgtxt = os.path.realpath(os.path.join(__file__, '..', 'build', 'imgtxtenh'))


def run_imgtxtenh(in_img:str, out_img:str, options:list[str]=None) -> None:
    """
    Run the imgtxtenh program with the given input image and options.

    Args:
        in_img (str): Path to the input image file.
        out_img (str): Path to the output image file.
        options (list, optional): List of option strings to pass to the program.

    Returns:
        subprocess.Popen: The Popen object representing the running process.
    """
    cmd = [imgtxt]

    if options:
        cmd.extend(options)

    cmd.append(in_img)
    cmd.append(out_img)

    Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()


if __name__ == '__main__':
    in_img_path = "/home/tz/documents/imgtxtenh/sample/13221_16.jpg"
    out_img_path = "output.jpg"
    options = ["-t", "wolf", "-w", "100", "-k", "0.3", "-s", "0.6"]

    run_imgtxtenh(in_img_path, out_img_path, options)

    import cv2
    img = cv2.imread(out_img_path)
    cv2.imshow('fa', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
