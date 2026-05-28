import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Update chart colors
        content = content.replace("const C=['#3b82f6','#22c55e','#f59e0b','#8b5cf6','#06b6d4','#ef4444','#f97316'];",
                                  "const C=['#2563EB','#3B82F6','#10B981','#F59E0B','#8B5CF6','#06B6D4','#EF4444'];")
        content = content.replace("const TT={backgroundColor:'#131829',titleColor:'#f8fafc',bodyColor:'#94a3b8',borderColor:'rgba(255,255,255,.1)',borderWidth:1,padding:10};",
                                  "const TT={backgroundColor:'#172033',titleColor:'#E5E7EB',bodyColor:'#94A3B8',borderColor:'#243045',borderWidth:1,padding:12,cornerRadius:8,displayColors:true,boxPadding:4};")
        
        # Rounded bars and refined grids
        content = content.replace("backgroundColor:'#3b82f666',borderColor:'#3b82f6',borderWidth:1",
                                  "backgroundColor:'rgba(59, 130, 246, 0.6)',borderColor:'#3B82F6',borderWidth:0,borderRadius:4")
        content = content.replace("backgroundColor:'#8b5cf699',borderColor:'#8b5cf6',borderWidth:1",
                                  "backgroundColor:'rgba(139, 92, 246, 0.6)',borderColor:'#8B5CF6',borderWidth:0,borderRadius:4")
        content = content.replace("backgroundColor:'#22c55e66',borderColor:'#22c55e',borderWidth:1",
                                  "backgroundColor:'rgba(16, 185, 129, 0.6)',borderColor:'#10B981',borderWidth:0,borderRadius:4")
        content = content.replace("backgroundColor:'#f59e0b66',borderColor:'#f59e0b',borderWidth:1",
                                  "backgroundColor:'rgba(245, 158, 11, 0.6)',borderColor:'#F59E0B',borderWidth:0,borderRadius:4")
        content = content.replace("backgroundColor:['#3b82f699','#f59e0b99'],borderColor:'#0d1120',borderWidth:2",
                                  "backgroundColor:['#2563EB','#10B981'],borderColor:'#0B1120',borderWidth:3,borderRadius:4,hoverOffset:4")
        content = content.replace("backgroundColor:CA,borderColor:'#0d1120',borderWidth:2",
                                  "backgroundColor:CA,borderColor:'#0B1120',borderWidth:3,borderRadius:4,hoverOffset:4")
        
        # Grids
        content = content.replace("grid:{color:'rgba(255,255,255,.04)'}", "grid:{color:'#243045',drawBorder:false}")
        content = content.replace("color:var(--t1)", "color:var(--text-main)")
        content = content.replace("color:var(--t2)", "color:var(--text-muted)")

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Chart updates applied successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
