import sys

def main():
    try:
        with open('header.html', 'r', encoding='utf-8') as f:
            header_content = f.read()

        with open('index.html', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        script_start = 0
        for i, line in enumerate(lines):
            if line.strip() == '// ====== DADOS MOCK (1200 escolas, 5% estaduais) ======' or line.strip().startswith('const ROWS='):
                script_start = i
                # Go back up to the comment if possible
                if lines[i-1].strip().startswith('// ======') or lines[i-3].strip().startswith('// ======'):
                    script_start = i-3
                break

        if script_start == 0:
            print("Could not find script data start.")
            return

        script_content = "".join(lines[script_start:])

        new_html = header_content + "\n" + script_content

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
            
        print("Merged successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
