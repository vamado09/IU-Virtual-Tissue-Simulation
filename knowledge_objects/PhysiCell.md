## What Is PhysiCell

PhysiCell is an advanced agent-based simulation framework designed to simulate individual cells as software agents within a simulated tissue environment. This innovative tool allows for the detailed study of the dynamics and interactions of thousands or even millions of cells in three-dimensional (3-D) microenvironments, focusing on microenvironment-dependent phenotypes. PhysiCell agents are capable of implementing key cell-scale processes such as cell cycling and death, volume changes, mechanics, motility, and the secretion and uptake of diffusible substrates in the tissue microenvironment.

Each cell agent in PhysiCell is equipped with a variety of phenotypic parameters that regulate these processes. These parameters include the cell's position, volume (and sub-volumes), cell cycle or death status, secretion parameters, and mechanics (adhesive, deformation, and motility) parameters. The behavior of each agent is controlled by modulating these phenotypic parameters with cell functions that reflect our biological hypotheses on how each cell type responds to stimuli in the microenvironment.

PhysiCell utilizes a lattice-free, physics-based approach to minimize grid-based artifacts, providing optimized, biologically realistic functions for key cell behaviors. These behaviors include cell cycling (with multiple models for both in vitro and in vivo-focused simulations), cell death (apoptosis and necrosis), volume regulation (fluid and solid biomass; nuclear and cytoplasmic sub-volumes), motility, and cell-cell mechanical interactions. The framework is designed with a hierarchical Phenotype data structure for each cell agent, allowing users to model microenvironment-dependent triggers of standard cell processes easily, without the need to code these basic processes from scratch.

The flexibility of PhysiCell is one of its key strengths. Written in a modular manner, it allows users to extend, rewrite, or even replace its originally implemented functions to suit their specific research needs. This adaptability makes PhysiCell a powerful tool for a wide range of applications, from computational tissue engineering to cancer systems engineering. Furthermore, PhysiCell has been parallelized to support the dynamics and interactions of millions of cells in 3-D microenvironments efficiently.

Since its inception in Fall 2017, PhysiCell has been utilized in both undergraduate and graduate education as a self-contained tool, demonstrating its value not only in research but also as an educational resource. Additionally, PhysiCell serves as an independent codebase for cross-validating model predictions across various platforms such as Chaste, Biocellion, TiSim, Timothy, and others, highlighting its significance in the broader scientific community.

In summary, PhysiCell represents a cutting-edge tool in the field of computational biology, offering researchers and educators a robust framework for exploring the complex dynamics of cellular systems in 3-D microenvironments.

## Who Should Use PhysiCell

PhysiCell is a versatile agent-based simulation framework designed to simulate individual cells as software agents within a simulated tissue environment. Its capabilities make it an invaluable tool for a wide range of users interested in understanding and predicting the dynamics and interactions of cells in 3-D microenvironments. Here are the primary groups who would benefit from using PhysiCell:

### Researchers and Scientists in Computational Biology and Bioengineering
PhysiCell is ideal for researchers and scientists working in computational biology, bioengineering, and related fields. It allows for the simulation of thousands or millions of cells, making it suitable for studying complex biological systems, such as tumor growth, tissue regeneration, and the effects of various treatments on cellular behavior. Its physics-based approach reduces grid-based artifacts, providing more realistic simulations of cell behaviors and interactions.

### Educators in Undergraduate and Graduate Programs
Since Fall 2017, PhysiCell has been used as a self-contained tool in undergraduate and graduate education, particularly in computational tissue engineering and cancer systems engineering courses. Its user-friendly interface and comprehensive documentation make it an excellent resource for educators looking to introduce students to the principles of agent-based modeling and simulation in biological systems.

### Developers and Computational Modelers
PhysiCell's modular design allows developers and computational modelers to extend, rewrite, or replace its originally implemented functions to suit their specific research needs. This flexibility makes PhysiCell a powerful platform for developing custom simulations and exploring large spaces of parameter values and hypotheses with biophysically realistic, 3-D models.

### Precision Medicine and Heterogeneous Tumor Modeling
Researchers focusing on precision medicine and heterogeneous tumor modeling will find PhysiCell particularly useful. It supports the dynamics and interactions of cells with microenvironment-dependent phenotypes, enabling the exploration of tumor heterogeneity and the development of personalized treatment strategies based on simulated tumor growth and response to therapies.

### Cross-Validation and Collaboration
PhysiCell also serves as an independent codebase for cross-validating model predictions with other platforms such as Chaste, Biocellion, TiSim, Timothy, and more. This makes it an excellent tool for collaborative research projects aiming to verify and improve the accuracy of computational models across different simulation environments.

In summary, PhysiCell is a powerful and flexible tool that caters to a broad audience, including researchers, educators, developers, and those involved in precision medicine. Its ability to simulate complex biological processes in 3-D microenvironments with high fidelity makes it a go-to framework for anyone interested in advancing our understanding of cellular dynamics and interactions.

## When Should I Use PhysiCell

PhysiCell is a versatile agent-based simulation framework designed for simulating the complex dynamics of individual cells within a simulated tissue environment. It is particularly well-suited for researchers, educators, and professionals in fields such as computational tissue engineering, cancer systems engineering, and precision medicine. Below are several scenarios and research areas where PhysiCell can be particularly beneficial:

### 1. **Studying Cell Dynamics and Interactions in 3-D Microenvironments**
If your research involves understanding how thousands or even millions of cells interact within three-dimensional microenvironments, PhysiCell offers a powerful platform. Its lattice-free, physics-based approach minimizes grid-based artifacts, providing a more realistic simulation of cell behaviors and interactions.

### 2. **Exploring Microenvironment-Dependent Phenotypes**
PhysiCell is designed to model how cells respond to various stimuli in their microenvironment. It allows for the simulation of cell cycling, death, volume regulation, motility, and cell-cell mechanical interactions, all dependent on the surrounding microenvironment. This makes it an excellent tool for investigating how different environmental factors influence cell behavior.

### 3. **Parameter Space Exploration and Hypothesis Testing**
Researchers looking to explore a large space of parameter values or test various biological hypotheses will find PhysiCell to be an efficient tool. Its biophysically realistic, 3-D models enable users to simulate complex biological processes and assess the impact of different parameters or rules on cell behavior and tissue dynamics.

### 4. **Educational Purposes**
PhysiCell has been successfully integrated into undergraduate and graduate education as a self-contained tool for teaching computational tissue engineering and cancer systems engineering. Its user-friendly interface and comprehensive documentation make it accessible for students learning about complex biological systems and computational modeling.

### 5. **Cross-Validation of Model Predictions**
For those involved in computational biology or bioinformatics, PhysiCell serves as an independent codebase that can be used to cross-validate model predictions with other platforms such as Chaste, Biocellion, TiSim, Timothy, and more. This capability is crucial for ensuring the accuracy and reliability of computational models in scientific research.

### 6. **Heterogeneous Tumor Modeling and Precision Medicine**
PhysiCell's ability to simulate the dynamics and interactions of cells with heterogeneous phenotypes makes it an invaluable tool for modeling tumor heterogeneity. This is particularly relevant for precision medicine, where understanding the variability within tumors can inform more targeted and effective treatment strategies.

In summary, PhysiCell is a comprehensive, flexible, and powerful tool for simulating cell behavior and interactions in 3-D microenvironments. Its wide range of applications, from basic biological research to clinical implications in precision medicine, makes it a valuable resource for anyone interested in the complex dynamics of multicellular systems.

## How Do I Learn About PhysiCell

Learning about PhysiCell, an agent-based simulation framework designed for simulating individual cells within a tissue environment, is a journey into the intersection of biology, physics, and computational modeling. Whether you're a student, researcher, or enthusiast in the fields of computational tissue engineering, cancer systems engineering, or precision medicine, there are several resources and strategies to help you get started and advance your understanding of PhysiCell.

### Official Documentation and Tutorials

The first step in learning about PhysiCell is to explore the [official PhysiCell documentation](http://physicell.org/documentation/). This comprehensive guide covers everything from the basic concepts of the framework to detailed instructions on how to set up and run simulations. The documentation is regularly updated to reflect the latest features and improvements.

### Research Papers and Publications

PhysiCell has been featured in numerous research papers and publications that demonstrate its applications in studying the dynamics and interactions of cells in 3-D microenvironments. Key papers include:

- Metzcar et al., 2019, which introduces PhysiCell as an agent-based simulation framework.
- Publications that discuss the use of PhysiCell in undergraduate and graduate education, and its role in computational tissue engineering and cancer systems engineering.
- Studies on heterogeneous tumor modeling and the implications of PhysiCell in precision medicine.

Reading these papers can provide you with a deeper understanding of PhysiCell's capabilities, applications, and the scientific principles it is based on.

### Online Courses and Workshops

Keep an eye out for online courses and workshops focused on computational biology and agent-based modeling. These educational events often include sessions on PhysiCell, providing hands-on experience and the opportunity to learn from experts in the field.

### Community Forums and Support

Joining the PhysiCell community can be incredibly beneficial. Platforms like GitHub, research group forums, and social media groups dedicated to computational biology and simulation modeling are great places to ask questions, share experiences, and connect with other PhysiCell users.

### Experimentation and Practice

Finally, the best way to learn about PhysiCell is by using it. Start with simple simulations using the examples provided in the documentation, and gradually experiment with modifying parameters, implementing new cell behaviors, and exploring different hypotheses. This hands-on experience is invaluable in understanding how PhysiCell works and how it can be applied to various research questions.

By leveraging these resources and actively engaging with the PhysiCell framework and its community, you'll gain a solid foundation in agent-based simulation and be well on your way to conducting your own innovative research with PhysiCell.

## Strengths

PhysiCell is a cutting-edge agent-based simulation framework that offers a comprehensive suite of features for simulating individual cells within a simulated tissue environment. Its strengths lie in its ability to model the dynamics and interactions of thousands to millions of cells in three-dimensional microenvironments, making it an invaluable tool in the fields of computational tissue engineering and cancer systems engineering. Below are some of the key strengths of PhysiCell:

- **Biologically Realistic Simulations**: PhysiCell implements key cell-scale processes such as cell cycling and death, volume changes, mechanics, motility, and the secretion and uptake of diffusible substrates in the tissue microenvironment. This allows for simulations that closely mimic real biological phenomena.

- **Microenvironment-Dependent Phenotypes**: The framework is designed to study cells in 3-D microenvironments with phenotypes that depend on their surroundings. This feature is crucial for understanding how cells interact with and adapt to their microenvironment, which is particularly relevant in cancer research and tissue engineering.

- **Lattice-Free, Physics-Based Approach**: By using a lattice-free approach, PhysiCell reduces grid-based artifacts, providing a more accurate representation of cell behavior and interactions. This physics-based approach ensures that simulations are grounded in realistic biological functions.

- **Modular and Extensible**: PhysiCell is written in a modular manner, allowing users to easily extend, rewrite, or replace its originally implemented functions. This flexibility makes it adaptable to a wide range of research needs and allows it to serve as a platform for innovation in computational biology.

- **Parallelized for Efficiency**: The system has been parallelized to support the dynamics and interactions of even millions of cells, making it capable of handling large-scale simulations efficiently. This is particularly important for exploring large spaces of parameter values and hypotheses with biophysically realistic, 3-D models.

- **Educational Tool**: Since Fall 2017, PhysiCell has been used in undergraduate and graduate education as a self-contained tool for computational tissue engineering and cancer systems engineering. This demonstrates its accessibility and potential to train the next generation of computational biologists.

- **Cross-Validation with Other Platforms**: PhysiCell serves as an independent codebase to cross-validate model predictions with other platforms such as Chaste, Biocellion, TiSim, Timothy, and more. This interoperability is crucial for ensuring the accuracy and reliability of simulation results across different computational models.

In summary, PhysiCell's strengths in providing biologically realistic, flexible, and efficient simulations make it a powerful tool for advancing research in computational biology, particularly in the areas of cancer research and tissue engineering. Its modular design, coupled with its ability to simulate complex cell dynamics in 3-D microenvironments, positions it as a leading framework in the field.

## Limitations

While PhysiCell offers a robust and flexible framework for simulating the dynamics and interactions of cells within 3-D microenvironments, it is important to acknowledge certain limitations inherent to the system. Understanding these limitations is crucial for researchers to effectively use PhysiCell in their studies and to interpret the results accurately.

1. **Parameter Sensitivity and Calibration**: One of the challenges in using PhysiCell involves the calibration of phenotypic rate parameters and the sensitivity of model outcomes to these parameters. Although PhysiCell allows for extensive customization of cell behaviors through phenotypic parameters, determining the accurate values for these parameters can be complex and time-consuming. This process often requires extensive experimental data for validation, which may not always be readily available.

2. **Computational Resources**: Simulating the dynamics of thousands or millions of cells in 3-D microenvironments, especially with microenvironment-dependent phenotypes, is computationally intensive. Users may encounter limitations related to the computational resources available to them, such as processing power and memory. This can affect the scale and complexity of the simulations that can be realistically performed.

3. **Modeling Assumptions**: Like all modeling frameworks, PhysiCell is based on a set of assumptions about cell behavior and interactions within the tissue microenvironment. These assumptions, while necessary for simplification and computational feasibility, may not fully capture the complexity of biological systems in vivo. Users must be cautious in extrapolating model predictions to real-world scenarios without considering the potential limitations of these assumptions.

4. **Learning Curve**: Despite the modular design intended to facilitate ease of use and extension, new users may face a steep learning curve. Understanding the hierarchical Phenotype data structure, modifying it to suit specific research needs, and integrating new or rewritten functions require a solid understanding of both the biological systems being modeled and the computational aspects of the framework.

5. **Interoperability with Other Tools**: While PhysiCell has been used to cross-validate model predictions with other platforms like Chaste, Biocellion, and Timothy, seamless interoperability with other computational tools and databases is not always straightforward. Users aiming to integrate PhysiCell simulations with other software tools or databases may need to invest additional effort in developing custom interfaces or conversion tools.

6. **Grid-Based Artifacts**: Although PhysiCell employs a lattice-free, physics-based approach to reduce grid-based artifacts, completely eliminating such artifacts in spatial simulations is challenging. Users should be aware of the potential for these artifacts to influence simulation outcomes, particularly in scenarios where spatial organization and cell-cell interactions are critical.

In conclusion, while PhysiCell is a powerful tool for simulating multicellular systems and exploring the effects of microenvironmental stimuli on cell behavior, users should be mindful of these limitations. Careful consideration of these factors, along with rigorous validation against experimental data, will enhance the reliability and applicability of PhysiCell simulations in biomedical research.

## Alternative Options

While PhysiCell offers a robust and flexible framework for simulating the dynamics and interactions of cells within 3-D microenvironments, there are several alternative platforms and tools available for researchers seeking different features or specialized functionalities. Below, we outline some of these alternatives, highlighting their unique strengths and potential applications.

### Chaste

**Chaste** (Cancer, Heart, and Soft Tissue Environment) is an open-source C++ library for the simulation of multi-scale, multi-physics problems in biology and physiology. It is particularly well-suited for modeling tissue mechanics, cardiac electrophysiology, and cancer development. Chaste's strength lies in its comprehensive set of tools for solving complex partial differential equations (PDEs) and its ability to handle simulations involving millions of cells. It is an excellent choice for researchers focused on cardiac dynamics or the mechanical aspects of tissue engineering.

### Biocellion

**Biocellion** is a high-performance computing (HPC) framework designed to simulate large-scale agent-based models with billions of cells. It is optimized for running on supercomputers, making it ideal for very large and computationally demanding simulations. Biocellion's key advantage is its scalability and efficiency, allowing researchers to explore vast parameter spaces and complex interactions within multicellular systems. It is particularly useful for studies in developmental biology, tissue engineering, and cancer research.

### CompuCell3D

**CompuCell3D** is a flexible, scriptable modeling environment for simulating the behavior of multicellular systems. It integrates cellular Potts models with differential equations to simulate cell growth, division, death, and migration, as well as the evolution of extracellular chemical fields. CompuCell3D's strength lies in its user-friendly interface and the ability to quickly prototype models without extensive programming knowledge. It is well-suited for educational purposes and for researchers new to computational biology.

### TiSim and Timothy

**TiSim** and **Timothy** are both specialized tools for tissue simulation. TiSim focuses on the mechanical properties and behaviors of tissues, offering detailed models for tissue deformation and stress responses. Timothy, on the other hand, is designed for simulating large-scale cellular systems, with a particular emphasis on the spatial organization and dynamics of cells within tissues. Both platforms offer unique perspectives on tissue modeling, with TiSim being more focused on mechanical aspects and Timothy on cellular interactions and organization.

### Summary

Each of these alternative platforms offers unique features and strengths, making them suitable for different types of research questions and modeling needs. Whether you are interested in detailed mechanical simulations, large-scale agent-based models, or user-friendly environments for educational purposes, there is likely a tool available that meets your requirements. Researchers are encouraged to explore these options to find the best fit for their specific projects and objectives.

## Example Deployments

PhysiCell, an advanced agent-based simulation framework, has been deployed in various research and educational settings, showcasing its versatility and power in simulating the complex dynamics of cellular systems. Below are some notable examples of PhysiCell deployments that highlight its capabilities and the breadth of its applications.

### Educational Use in Computational Tissue Engineering and Cancer Systems Engineering

Since Fall 2017, PhysiCell has been integrated into undergraduate and graduate education as a comprehensive tool for computational tissue engineering and cancer systems engineering. Its user-friendly nature and self-contained structure make it an excellent resource for students learning about the complexities of cellular behaviors and interactions within tissues. This educational deployment helps in nurturing the next generation of researchers by providing them with hands-on experience in computational modeling and simulation.

### Heterogeneous Tumor Modeling

One of the significant applications of PhysiCell is in the field of cancer research, particularly in modeling heterogeneous tumors. By leveraging its capabilities to simulate millions of cells within 3-D microenvironments, researchers can explore the dynamics of tumor growth, the interactions between different cell types within a tumor, and the impact of the tumor microenvironment on cancer progression. This application is crucial for understanding the mechanisms of tumor heterogeneity and for developing targeted cancer therapies.

### Precision Medicine Simulator

PhysiCell has also been utilized to create simulators for precision medicine. These simulators can model the interactions between various cell types and the microenvironment in specific patient-derived tumors. By simulating the effects of different therapeutic interventions on these personalized models, researchers can predict the most effective treatment strategies for individual patients. This deployment of PhysiCell represents a significant step towards the realization of precision medicine in oncology, where treatments are tailored to the unique genetic and phenotypic characteristics of a patient's tumor.

### Cross-Validation with Other Platforms

In addition to its standalone applications, PhysiCell serves as an independent codebase for cross-validating model predictions with other simulation platforms such as Chaste, Biocellion, TiSim, and Timothy. This interoperability is crucial for ensuring the accuracy and reliability of computational models in biological research. By comparing and validating results across different platforms, researchers can have greater confidence in their simulations and the biological insights they provide.

### Conclusion

These example deployments of PhysiCell demonstrate its flexibility, power, and potential to revolutionize our understanding of cellular systems and to advance the fields of computational biology, tissue engineering, and precision medicine. As the PhysiCell community continues to grow and the framework evolves, we can expect to see even more innovative and impactful applications in the future.

## References

- Metzcar, J., Wang, Y., Heiland, R., & Macklin, P. (2019). Agent-based computational modeling of glioblastoma predicts that stromal density is central to oncolytic virus efficacy. *Agent-based computational modeling of--glioblastoma*.

- Macklin, P., Edgerton, M. E., Thompson, A. M., & Cristini, V. (2023). PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems. *PhysiCell_An open source physics-based cell simulator for 3-D multicellular systems*.

- Ghaffarizadeh, A., Heiland, R., Friedman, S. H., Mumenthaler, S. M., & Macklin, P. (2023). Heterogeneous Tumour Modeling Using PhysiCell and Its Implications in Precision Medicine. *Heterogeneous Tumour Modeling Using PhysiCell and Its Implications in Precision Medicine*.