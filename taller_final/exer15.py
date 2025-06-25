"""
Usando la librería re, crea funciones para:
· Validar direcciones de email
· Extraer números de teléfono de un texto
· Limpiar y formatear texto (eliminar caracteres especiales)
"""
import re


def validate_email(e):
    if re.fullmatch(r'[a-zA-Z0–9._%+-]+@[a-zA-Z0–9.-]+\.[a-zA-Z]{2,}', e):
        print('Valido')
        return
    print('Invalido')


def extract_phones(t):
    phone_numbers= re.findall(r'\+?\d{1,4}?[-.\s]?(?:\d{1,3}?)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}', t, re.M)
    return f'List phone numbers:\n{phone_numbers}'


def replace_special(t):
    return re.sub(r'[\W\.,)(!]', ' ', t)


validate_email('Juandavid@gmail.com')  # Valid
validate_email('aguirre123-/@..gmail.  com')  # Invalid

text= """For any inquiries, you can reach our main office at 555-123-4567. If you need to speak with customer service, their direct line is 555-987-6543. You can also try our support hotline, available 24/7, at 555-246-8000. For international callers, please use +1-555-111-2222. Colombian number test +57 315 6987559""" 
print(extract_phones(text))  # List of phone numbers

text= """You can always reach out to us via email at info@example.com, or connect with us on social media! Find us on X (formerly Twitter) @ExampleCorp, or on Facebook at /ExampleCorp. For urgent matters, try our emergency line at (555) 123-4567, or send a fax to +1-555-987-6543. We appreciate your patience & understanding!"""
print(replace_special(text))  # No special chars in it

