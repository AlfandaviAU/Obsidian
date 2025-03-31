## [`str.isdigit`](https://docs.python.org/3/library/stdtypes.html#str.isdigit)

> Return true if all characters in the string are digits and there is at least one character, false otherwise. **Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal**.

## [`str.isnumeric`](https://docs.python.org/3/library/stdtypes.html#str.isnumeric)

> Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise. **Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric**.

## [`str.isdecimal`](https://docs.python.org/3/library/stdtypes.html#str.isdecimal)

> Return true if all characters in the string are decimal characters and there is at least one character, false otherwise. **Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character is a character in the Unicode General Category “Nd”**.
> 