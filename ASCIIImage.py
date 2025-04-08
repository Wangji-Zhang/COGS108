from PIL import Image

# 定义字符集（按灰度从深到浅排列）
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 将像素值映射为字符
def pixel_to_char(pixel_value):
    # 将像素值（0-255）映射到字符集索引（0-9）
    return ASCII_CHARS[min(pixel_value // 25, len(ASCII_CHARS) - 1)]

# 将图片转换为字符画
def image_to_ascii(image_path, output_width=100):
    try:
        # 打开图片并转换为灰度图
        image = Image.open(image_path).convert("L")
    except Exception as e:
        print(f"无法打开图片: {e}")
        return

    # 获取图片原始尺寸
    width, height = image.size
    # 计算输出高度（保持宽高比）
    aspect_ratio = height / width
    output_height = int(aspect_ratio * output_width * 0.55)  # 调整高度比例
    # 调整图片大小
    image = image.resize((output_width, output_height))
    # 将每个像素转换为字符
    pixels = image.getdata()
    ascii_str = "".join(pixel_to_char(pixel) for pixel in pixels)
    # 按宽度分行
    ascii_lines = [ascii_str[i:i+output_width] for i in range(0, len(ascii_str), output_width)]
    return "\n".join(ascii_lines)

# 示例用法
if __name__ == "__main__":
    image_path = "C:\\Programming\\trashBin\\e1f4cd45d41cf9a5ca97c5418413729.jpg"  # 替换为你的图片路径
    output_width = 100  # 设置输出宽度
    ascii_art = image_to_ascii(image_path, output_width)
    if ascii_art:
        print(ascii_art)


