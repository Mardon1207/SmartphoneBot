from PIL import Image, ImageDraw, ImageFont

def create_certificate(user_name, result, vaqt, ismi):
    # Sertifikat shablonini yuklab oling
    template = Image.open('Sertifikat1.png')
    draw = ImageDraw.Draw(template)

    # Shrift va rangni tanlang
    natija = ImageFont.truetype('times.ttf', 30)
    ism = ImageFont.truetype('times.ttf', 70)
    sana = ImageFont.truetype('times.ttf', 45)
    muallif = ImageFont.truetype('times.ttf', 45)
    color = 'rgb(0, 0, 0)'  # qora

    # Matn joylashuvini o'lchang
    text_bbox = draw.textbbox((0, 0), user_name, font=ism)
    text_width = text_bbox[2] - text_bbox[0]
    image_width = template.width
    start_x = (image_width - text_width) / 2

    # Matnni joylashtirish
    draw.text((start_x, 565), f"{user_name}", fill=color, font=ism)
    draw.text((612, 752), f"{result}", fill=color, font=natija)
    draw.text((530, 956), f"{vaqt}", fill=color, font=sana)
    draw.text((1320, 956), f"{ismi}", fill=color, font=muallif)

    # Yaratilgan sertifikatni saqlang
    output_path = f"certificate.jpg"
    template.save(output_path)
    return output_path