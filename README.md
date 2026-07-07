# CNC Engineering Course

**Author**: Todd | **Company**: Hendrixx Design | **Contact**: todd@hendrixxdesign.com

## CNC Gantry Design Course

A comprehensive, open-source guide for makers, engineers, and innovators who want to master the art and science of modern CNC systems.

---

## 📖 Course Overview

This course provides in-depth knowledge about designing, building, and optimizing CNC gantry systems. Whether you're building a plasma cutter, router, laser cutter, water jet, or hybrid machine, this course covers everything from mechanical design to advanced control systems.

**What You'll Learn:**
- Mechanical frame design and structural analysis
- Motor selection and drive systems (steppers, servos)
- Linear motion systems (ball screws, rack & pinion, linear guides)
- Control electronics and motion controllers
- Tool-specific modules (plasma, spindle, fiber laser, water jet)
- Advanced systems (pick & place, robotic arms, large-format FDM printers)
- CAD design and modeling for CNC manufacturing
- CAM programming and toolpath generation
- G-code programming and optimization
- Quality management systems and metrology
- Shop organization and L.E.A.N. manufacturing strategies
- Business ownership and management
- EMI/EMC considerations and safety protocols

---

## 🎯 Who Is This Course For?

- **Makers & Hobbyists** looking to build their first CNC machine
- **Engineers** designing professional-grade CNC systems
- **Educators** teaching manufacturing and mechatronics
- **Entrepreneurs** developing CNC-based products
- **Students** learning about precision motion control

---

## 📚 Course Modules

### Foundation Modules (1-4)
- `Module-01-Mechanical-Frame-and-Structure`
- `Module-02-Vertical-Axis-and-Z-Stage`
- `Module-03-Linear-Motion-Systems`
- `Module-04-Control-Electronics`

### Tool-Specific Modules (5-8)
- `Module-05-Plasma-Cutting`
- `Module-06-Spindle-and-Rotary-Tools`
- `Module-07-Fiber-Laser`
- `Module-08-Waterjet-Cutting`

### Advanced and Hybrid Systems (9-12)
- `Module-09-Pick-and-Place-Robot`
- `Module-10-Robotic-Arm`
- `Module-11-Large-Format-FDM-3D-Printing`
- `Module-12-Water-Jet-Guided-Laser-Cutting`

### Control, Software, and Process Engineering (13-20)
- `Module-13-EMI-EMC-for-Motion-Control`
- `Module-14-LinuxCNC-HAL-and-Real-Time-Control`
- `Module-15-G-Code-Standards-and-Post-Processing`
- `Module-16-CAD-Design-for-Manufacturable-Parts`
- `Module-17-Advanced-Materials-Composites-and-Ceramics`
- `Module-18-Industry-4-0-for-CNC-Manufacturing`
- `Module-19-Advanced-Control-Systems`
- `Module-20-Feeds-and-Speeds`

### Professional and Business Modules (21-26)
- `Module-21-Metrology-and-Precision-Measurement`
- `Module-22-Quality-Management-Systems-QMS`
- `Module-23-Shop-Organization-and-Management`
- `Module-24-LEAN-Strategies-for-CNC-Manufacturing`
- `Module-25-Work-Life-Balance-in-CNC-Manufacturing`
- `Module-26-CNC-Business-Ownership-and-Management`

### Appendices
- **Appendix A-P**: Material Properties, Hardware Specs, Motor Sizing, Linear Motion, Electrical Standards, G-code Reference, Safety Standards, Lubrication, Conversions, Troubleshooting, Vendors, Resources, Glossary, Contact, Updates, Mathematics
- **Appendix S**: L.E.A.N. Manufacturing Templates (2,910 lines)
- **Appendix T**: Business Ownership Templates (6,612 lines)

**Total**: 26 Comprehensive Modules + 20 Appendices

---

## 🚀 Getting Started

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/hendrixx-cnc/CNC-Engineering-Course-.git
   cd CNC-Engineering-Course-
   ```

2. **Start with the Course Foreword**
   - Read `Print/course-foreword.md` for an introduction and inspiration

3. **Follow the modules in sequence**
   - Begin with foundational modules (1-4)
   - Then explore tool-specific modules based on your project
   - Finish with control and programming modules

4. **Reference the appendix**
   - Use the files in `Appendices/` for formulas, conversions, and troubleshooting

---

## Repository Layout

- `Module-01-*` through `Module-26-*` - primary course source, with titled module folders in course order
- `Appendices/` - formulas, conversions, references, templates, and troubleshooting material
- `Print/` - front matter used for printable/PDF editions
- `PDFs/` - generated PDF exports, with compressed copies in `PDFs/optimized/`
- `Communication/` - AI collaboration notes and project communication files
- `Legacy-Modules/` - archived older course material kept for reference
- `tools/pdf/` - PDF and HTML generation utilities
- `build/` - generated local artifacts such as temporary Markdown, HTML, logs, and LaTeX
- `website/` - static website build script, content, and viewer

## Build Utilities

Run these from the repository root:

```bash
python3 tools/pdf/generate_pdfs.py
python3 tools/pdf/optimize_pdfs.py
python3 tools/pdf/generate_pdfs_simple.py
python3 website/build.py
```

## GitHub Pages

The repository includes `.github/workflows/pages.yml`, which builds `website/content/` from the root-level `Module-XX-*` folders and publishes the static site from `website/`. The workflow also copies `PDFs/` into the Pages artifact so module PDF links work on the live site while the PDF files remain in the repository's `PDFs/` folder.

The live site also publishes generated reference data from `website/data/`:

- `glossary.json` - searchable glossary terms from Appendix M
- `resources.json` - structured books, tools, standards, communities, and suppliers from Appendix L
- `link-graph.json` - module, glossary, resource, and appendix relationships for graph exploration

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

- **Report Issues**: Found a typo or error? [Open an issue](https://github.com/hendrixx-cnc/CNC-Engineering-Course-/issues)
- **Suggest Improvements**: Have ideas for new content? Submit a pull request
- **Share Your Builds**: Show us what you've created with this knowledge
- **Translate**: Help make this course accessible in other languages

Please use GitHub issues and pull requests for contribution discussion.

---

## 📄 License

This course and all its materials are licensed under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** License.

**You are free to:**
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original

See https://creativecommons.org/licenses/by-sa/4.0/ for full details.

---

## 🌟 Acknowledgments

This course is the result of collaboration between:
- Hendrixx CNC Team
- GitHub Copilot
- CNC Zone Community Members
- OpenBuilds Supporters
- MIT OpenCourseWare Educators

Special thanks to all engineers, makers, and educators who contributed advice and feedback.

See [Course Acknowledgments](Print/course-acknowledgments.md) for full details.

---

## 📞 Contact & Community

- **GitHub Issues**: [hendrixx-cnc/CNC-Engineering-Course-](https://github.com/hendrixx-cnc/CNC-Engineering-Course-/issues)
- **Email**: info@hendrixx-cnc.com
- **Community**: Join our discussions and share your projects

---

## 🔧 Course Status

**Current Version**: v1.1

See `Appendices/appendix-O-updates.md` for update history and planned features.

---

**Every great machine started as a spark of imagination. Let this course be your launchpad. Build with curiosity, learn with persistence, and create with passion.**
