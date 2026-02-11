---
title: "发表论文"
layout: "simple"
fullWidth: true
---

<!-- 引入 FontAwesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- 引入自定义样式 -->
{{< publications_css >}}

<div class="pub-content">

<!-- 统计栏 (数据需根据实际情况微调) -->
{{< publications_stats 
    total="30" 
    first="15" 
    impact="167.3" 
    citations="473" 
>}}

<!-- 搜索和筛选 -->
{{< publications_search >}}


> "*" 代表通讯作者


<!-- 论文列表 -->
<div class="pub-list" id="publicationList">
    <!-- ================================================================================== -->
    <!-- 2026 Papers -->
    <!-- ================================================================================== -->
    {{< publication_item
        title="注CO<sub>2</sub>提高天然气采收率中CO<sub>2</sub>-CH<sub>4</sub>过渡带演化规律研究"
        year="2026"
        type="journal"
        tags="ai,denoising"
        search="self-supervised denoising"
        authors="<span class='author-me'>高鑫远</span>, 杨胜来*, 位云生, 闫海军, 彭先, 李隆新, 赵梓寒, 姜艺, 王梦雨, 刘晓旭"
        meta="<span><i class='fas fa-calendar'></i> 2026</span><span><i class='fas fa-book'></i> 中国石油大学学报(自然科学版)</span><span><i class='fas fa-star'></i> IF: 3.2</span><span><i class='fas fa-quote-right'></i> Citations: 0</span>"
        bibtexId="bib202601"
        bibtexKey="gu2026thz"
        bibtexContent="@article{gao2023influence,title={Influence of reservoir spatial heterogeneity on a multicoupling process of CO2 geological storage},author={Gao, Xinyuan and Yang, Shenglai and Shen, Bin and Tian, Lerao and Li, Shuai and Zhang, Xing and Wang, Jiatong},journal={Energy \& Fuels},volume={37},number={19},pages={14991--15005},year={2023},publisher={ACS Publications}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <button class="btn-action" onclick="toggleBibtex('bib202601')"><i class="fas fa-quote-right"></i> BibTeX</button>
    {{< /publication_item >}}
    {{< publication_item
        title="Numerical modeling of CO<sub>2</sub> storage and gas recovery enhancement in low-permeability carbonate reservoirs via acid-fractured horizontal wells"
        year="2026"
        type="journal"
        tags="ai,denoising"
        search="self-supervised denoising"
        authors="Jiangtao Hu, Shenglai Yang, Lufei Bi, <span class='author-me'>Xinyuan Gao</span>, Hui Deng, Ermeng Zhao*"
        meta="<span><i class='fas fa-calendar'></i> 2026</span><span><i class='fas fa-book'></i> Fuel</span><span><i class='fas fa-star'></i> IF: 7.5</span><span><i class='fas fa-quote-right'></i> Citations: 1</span>"
        bibtexId="bib202601"
        bibtexKey="gu2026thz"
        bibtexContent="@article{gao2023influence,title={Influence of reservoir spatial heterogeneity on a multicoupling process of CO2 geological storage},author={Gao, Xinyuan and Yang, Shenglai and Shen, Bin and Tian, Lerao and Li, Shuai and Zhang, Xing and Wang, Jiatong},journal={Energy \& Fuels},volume={37},number={19},pages={14991--15005},year={2023},publisher={ACS Publications}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <button class="btn-action" onclick="toggleBibtex('bib202601')"><i class="fas fa-quote-right"></i> BibTeX</button>
    {{< /publication_item >}}
    <!-- ================================================================================== -->
    <!-- 2025 Papers -->
    <!-- ================================================================================== -->
    {{< publication_item
        title="Pore-scale modeling of multiple fluids flow transport kinetics for CO<sub>2</sub> enhanced gas recovery"
        year="2025"
        type="journal"
        tags="ai,imaging,selected"
        award="连续四期ESI高被引论文"
        search="self-supervised biomedical optical imaging"
        authors="<span class='author-me'>Xinyuan Gao</span>*, Shenglai Yang, Beidong Wang, Yiqi Zhang*, Jiangtao Hu, Mengyu Wang, Bin Shen*, Ermeng Zhao"
        venue="Energy"
        venueStyle="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i>Energy</span><span><i class='fas fa-star'></i> IF: 9.4</span><span><i class='fas fa-quote-right'></i> Citations: 33</span>"
        bibtexId="bib1"
        bibtexKey="gu2025enhancing"
        bibtexContent="@article{gu2025enhancing, title={Enhancing Biomedical Optical Volumetric Imaging via Self-Supervised Orthogonal Learning}, author={Gu, Yuanjie and Wang, Yiqun and Xuan, Ang and Wang, Jianping and Wang, Linyi and Zhang, Lei and Li, Xiaoran and Wu, Yao and Zhang, Jun and Lu, Zhi and Dong, Biqin}, journal={Science Advances}, year={2025}}"
    >}}
        <a href="https://gaoxy1118.github.io/assets/pdf/4Energy.pdf" download class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib1')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="https://www.biorxiv.org/content/10.1101/2025.05.16.654259v1" class="btn-action"><i class="fas fa-external-link-alt"></i> bioRxiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Wellbore-reservoir and multiphysics coupling model for liquid CO<sub>2</sub> cyclic injection in a CCUS-EGR framework"
        year="2025"
        type="journal"
        tags="ai,neuroscience,selected"
        award="连续两期ESI高被引论文"
        search="real-time self-supervised denoising neural imaging"
        authors="<span class='author-me'>Xinyuan Gao</span>, Shenglai Yang, Beidong Wang, Yiqi Zhang, Jiangtao Hu, Mengyu Wang, Bin Shen, Ermeng Zhao, Zhenhua Rui*"
        venue="Journal of Hydrology"
        venueStyle="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i>J. Hydrol.</span><span><i class='fas fa-star'></i> IF:6.3</span><span><i class='fas fa-quote-right'></i> Citations:26</span>"
        bibtexId="bib2"
        bibtexKey="wang2025realtime"
        bibtexContent="@article{wang2025realtime, title={Real-time Self-supervised Denoising for High-speed Fluorescence Neural Imaging}, author={Wang, Yiqun and Gu, Yuanjie and Wang, Jianping and Xuan, Ang and Kong, Cihang and Fang, Wei-Qun and Li, Dongyu and Zhu, Dan and Ding, Fengfei and Dong, Biqin}, journal={Nature Communications}, volume={16}, pages={9396}, year={2025}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib2')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Pore-scale simulation of multi-fluid flow transport dynamics for hydrogen geological storage in depleted gas reservoirs"
        year="2025"
        type="journal"
        tags="ai,microscopy"
        search="fluorescence microscopy denoising neural dynamics"
        authors="<span class='author-me'>Xinyuan Gao</span>, Shenglai Yang, Lufei Bi, Yiqi Zhang, Jiangtao Hu, Mengyu Wang, Bin Shen, Ermeng Zhao*"
        venue="Gondwana Research"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i> Gondwana Res.</span><span><i class='fas fa-star'></i> IF: 8.6</span><span><i class='fas fa-quote-right'></i> Citations: 8</span>"
        bibtexId="bib3"
        bibtexKey="gu2025gama"
        bibtexContent="@article{gu2025gama, title={GaMA: Stochastic Gaussian-masked Denoiser for Enhanced Fluorescence Microscopy of Subcellular Structures and Neural Dynamics}, author={Gu, Yuanjie and Wang, Yiqun and Zhao, Zhenyao and Lu, Jun and Xu, Lei and Lu, Zhi and Dong, Biqin}, journal={Advanced Technology in Neuroscience}, volume={3}, pages={1-5}, year={2025}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib3')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="A technical review of CO<sub>2</sub> flooding sweep-characteristics research advance and sweep-extend technology"
        year="2025"
        type="journal"
        tags="ai,medical imaging"
        award="ESI热点论文、连续四期高被引论文"
        search="fundus photography unpaired learning enhancement"
        authors="Yiqi Zhang, Shenglai Yang*, Lufei Bi, <span class='author-me'>Xinyuan Gao</span>*, Bin Shen, Jiangtao Hu, Yun Luo, Yang Zhao, Hao Chen, Jing Li"
        venue="Petroleum Science"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i> Pet. Sci.</span><span><i class='fas fa-star'></i> IF: 6.1</span><span><i class='fas fa-quote-right'></i> Citations: 52</span>"
        bibtexId="bib4"
        bibtexKey="gu2025automated"
        bibtexContent="@article{gu2025automated, title={Automated Enhanced Handheld Fundus Photography via Unpaired Learning}, author={Gu, Yuanjie and Yang, Jiacheng and Wang, Yiqun and Ye, Mengwen and Li, Xin and Li, Xiaoran and Li, Na and Zhang, Jun and Zhao, Yitian and Yu, Zekuan and Dong, Biqin}, journal={IEEE Transactions on Instrumentation and Measurement}, volume={74}, pages={1-12}, year={2025}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib4')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Visual characterization, exergy and mechanism analysis of in-situ nonequilibrium dynamic phase-behavior of CO<sub>2</sub>-oil"
        year="2025"
        type="journal"
        tags="ai,medical"
        search="skin cancer diagnosis optical attenuation"
        authors="Yiqi Zhang, Shenglai Yang*, Yun Luo, Yuning Han, Lerao Tian, Qing Liu, <span class='author-me'>Xinyuan Gao</span>*, Bin Shen*, Renfeng Yang, Jing Li"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i> Energy</span><span><i class='fas fa-star'></i> IF: 9.4</span><span><i class='fas fa-quote-right'></i> Citations: 15</span>"
        bibtexId="bib13"
        bibtexKey="zhang2025automated"
        bibtexContent="@article{zhang2025automated, title={Automated Diagnosis of Non-Melanoma Skin Cancer: A Joint Learning Approach Using Optical Attenuation Coefficients}, author={Zhang, Lei and Li, Xiaoran and Chen, Wen and Gu, Yuanjie and Wu, Hao and Lu, Zhong and Dong, Biqin}, journal={npj Digital Medicine}, volume={8}, pages={232}, year={2025}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib13')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Evaluation of the influence of gas impurities on sweep characteristics of impure-CO2 flooding in offshore fossil hydrogen energy development at pore scale: Insight from LF-NMR"
        year="2025"
        type="journal"
        tags="ai,federated learning"
        search="federated learning fundus image segmentation"
        authors="Yiqi Zhang, Shenglai Yang*, Yuning Han, Yun Luo, Qing Liu, Jiangtao Hu*, Bin Shen, Renfen Yan, Linjun Min, <span class='author-me'>Xinyuan Gao</span>*, Jing Li"
        venue="Physics of Fluids"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i> Phys. Fluids</span><span><i class='fas fa-star'></i> IF: 4.3</span><span><i class='fas fa-quote-right'></i> Citations: 3</span>"
        bibtexId="bib14"
        bibtexKey="yang2025fedgfm"
        bibtexContent="@article{yang2025fedgfm, title={Fed-GFM-DG: A Privacy-Preserving Framework for Fundus Image Segmentation via Generative-based Feature Generalization and Mask-Guided Aggregation}, author={Yang, Jiacheng and Gu, Yuanjie and Gao, Shujian and Ren, Wei and Yu, Zekuan}, journal={Biomedical Signal Processing and Control}, volume={106}, pages={1-14}, year={2025}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib14')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="The Characteristics and Parameter Correlation of Pore–Throat Structure in Ultradeep Carbonate Gas Reservoir Based on Dual-Resolution Computed Tomography Scanning"
        year="2025"
        type="journal"
        tags="ai,federated learning"
        search="federated learning fundus image segmentation"
        authors="Beidong Wang, Shenglai Yang*, Yulong Dang, <span class='author-me'>Xinyuan Gao</span>*, Jiangtao Hu*, Kun Yang, Shuai Zhao, Yiqi Zhang"
        venue="Energy & Fuels"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i> Energy Fuels</span><span><i class='fas fa-star'></i> IF: 5.3</span><span><i class='fas fa-quote-right'></i> Citations: 0</span>"
        bibtexId="bib14"
        bibtexKey="yang2025fedgfm"
        bibtexContent="@article{yang2025fedgfm, title={Fed-GFM-DG: A Privacy-Preserving Framework for Fundus Image Segmentation via Generative-based Feature Generalization and Mask-Guided Aggregation}, author={Yang, Jiacheng and Gu, Yuanjie and Gao, Shujian and Ren, Wei and Yu, Zekuan}, journal={Biomedical Signal Processing and Control}, volume={106}, pages={1-14}, year={2025}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib14')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Numerical simulation of CO<sub>2</sub> storage with enhanced gas recovery in depleted highly heterogeneous carbonate gas reservoir"
        year="2025"
        type="journal"
        tags="ai,federated learning"
        search="federated learning fundus image segmentation"
        authors="Jiangtao Hu*, Shenglai Yang*, Haiwei Zuo, Yubo Liu, Bin Shen, <span class='author-me'>Xinyuan Gao</span>, Hui Deng"
        venue="Physics of Fluids"
        meta="<span><i class='fas fa-calendar'></i> 2025</span><span><i class='fas fa-book'></i> Phys. Fluids</span><span><i class='fas fa-star'></i> IF: 4.3</span><span><i class='fas fa-quote-right'></i> Citations: 3</span>"
        bibtexId="bib14"
        bibtexKey="yang2025fedgfm"
        bibtexContent="@article{yang2025fedgfm, title={Fed-GFM-DG: A Privacy-Preserving Framework for Fundus Image Segmentation via Generative-based Feature Generalization and Mask-Guided Aggregation}, author={Yang, Jiacheng and Gu, Yuanjie and Gao, Shujian and Ren, Wei and Yu, Zekuan}, journal={Biomedical Signal Processing and Control}, volume={106}, pages={1-14}, year={2025}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib14')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    <!-- ================================================================================== -->
    <!-- 2024 Papers -->
    <!-- ================================================================================== -->
    {{< publication_item
        title="Deep-learning-assisted spectroscopic single-molecule localization microscopy based on spectrum-to-spectrum denoising"
        year="2024"
        type="journal"
        tags="ai,microscopy"
        search="single-molecule localization microscopy denoising"
        authors="Dandan Xu, <span class='author-me'>Yuanjie Gu</span>, Jun Lu, Lei Xu, Wei Wang, Biqin Dong*"
        venue="Nanoscale"
        meta="<span><i class='fas fa-calendar'></i> 2024</span><span><i class='fas fa-book'></i> Nanoscale</span><span><i class='fas fa-star'></i> IF: ~6.7</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib15"
        bibtexKey="xu2024deeplearning"
        bibtexContent="@article{xu2024deeplearning, title={Deep-learning-assisted spectroscopic single-molecule localization microscopy based on spectrum-to-spectrum denoising}, author={Xu, Dandan and Gu, Yuanjie and Lu, Jun and Xu, Lei and Wang, Wei and Dong, Biqin}, journal={Nanoscale}, volume={16}, number={11}, pages={5729-5736}, year={2024}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib15')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Super Resolution Reconstruction of Fluorescence Microscopy Image by Convolutional Network with Physical Priors"
        year="2024"
        type="journal"
        tags="ai,imaging"
        search="super-resolution fluorescence microscopy physical priors"
        authors="Qiangyu Cai, Jun Lu, Wenting Gu, Di Xiao, Boyi Li, Lei Xu, <span class='author-me'>Yuanjie Gu</span>, Biqin Dong, Xin Liu*"
        venue="Biomedical Optics Express"
        meta="<span><i class='fas fa-calendar'></i> 2024</span><span><i class='fas fa-book'></i> BOE</span><span><i class='fas fa-star'></i> IF: ~3.4</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib16"
        bibtexKey="cai2024super"
        bibtexContent="@article{cai2024super, title={Super Resolution Reconstruction of Fluorescence Microscopy Image by Convolutional Network with Physical Priors}, author={Cai, Qiangyu and Lu, Jun and Gu, Wenting and Xiao, Di and Li, Boyi and Xu, Lei and Gu, Yuanjie and Dong, Biqin and Liu, Xin}, journal={Biomedical Optics Express}, volume={15}, number={11}, pages={6638-6653}, year={2024}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib16')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    <!-- ================================================================================== -->
    <!-- 2023 Papers -->
    <!-- ================================================================================== -->
    {{< publication_item
        title="SegCoFusion: An Integrative Multimodal Volumetric Segmentation Cooperating with Fusion Pipeline to Enhance Lesion Awareness"
        year="2023"
        type="journal"
        tags="ai,segmentation"
        search="multimodal volumetric segmentation lesion awareness"
        authors="<span class='author-me'>Yuanjie Gu</span>#, Yinghan Guan#, Zekuan Yu*, Biqin Dong*"
        venue="IEEE Journal of Biomedical and Health Informatics"
        meta="<span><i class='fas fa-calendar'></i> 2023</span><span><i class='fas fa-book'></i> IEEE JBHI</span><span><i class='fas fa-star'></i> IF: ~7.7</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib5"
        bibtexKey="gu2023segcofusion"
        bibtexContent="@article{gu2023segcofusion, title={SegCoFusion: An Integrative Multimodal Volumetric Segmentation Cooperating with Fusion Pipeline to Enhance Lesion Awareness}, author={Gu, Yuanjie and Guan, Yinghan and Yu, Zekuan and Dong, Biqin}, journal={IEEE Journal of Biomedical and Health Informatics}, volume={27}, number={12}, pages={5860-5871}, year={2023}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib5')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Physics Driven Deep Retinex Fusion for Adaptive Infrared and Visible Image Fusion"
        year="2023"
        type="journal"
        tags="ai,image fusion"
        award="SPIE Wechat Highlight Paper"
        search="infrared visible image fusion retinex"
        authors="<span class='author-me'>Yuanjie Gu</span>, Zhibo Xiao, Yinghan Guan, Haoran Dai, Cheng Liu, Liang Xue, Shouyu Wang*"
        venue="Optical Engineering"
        meta="<span><i class='fas fa-calendar'></i> 2023</span><span><i class='fas fa-book'></i> Opt. Eng.</span><span><i class='fas fa-star'></i> IF: ~1.3</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib7"
        bibtexKey="gu2023physics"
        bibtexContent="@article{gu2023physics, title={Physics Driven Deep Retinex Fusion for Adaptive Infrared and Visible Image Fusion}, author={Gu, Yuanjie and Xiao, Zhibo and Guan, Yinghan and Dai, Haoran and Liu, Cheng and Xue, Liang and Wang, Shouyu}, journal={Optical Engineering}, volume={62}, number={8}, pages={083101}, year={2023}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib7')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Deep SBP+: Breaking Through the Space-bandwidth Product Limit based on a Physical-driven Cycle Constraint Framework"
        year="2023"
        type="journal"
        tags="ai,imaging"
        search="space-bandwidth product limit cycle constraint"
        authors="Zhibo Xiao#, <span class='author-me'>Yuanjie Gu</span>#, Lin Zhu, Cheng Liu, Shouyu Wang*"
        venue="Journal of the Optical Society of America A"
        meta="<span><i class='fas fa-calendar'></i> 2023</span><span><i class='fas fa-book'></i> JOSA A</span><span><i class='fas fa-star'></i> IF: ~1.8</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib10"
        bibtexKey="xiao2023deep"
        bibtexContent="@article{xiao2023deep, title={Deep SBP+: Breaking Through the Space-bandwidth Product Limit based on a Physical-driven Cycle Constraint Framework}, author={Xiao, Zhibo and Gu, Yuanjie and Zhu, Lin and Liu, Cheng and Wang, Shouyu}, journal={Journal of the Optical Society of America A}, volume={40}, number={5}, pages={833-840}, year={2023}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib10')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Deep-Gamma: Deep Low-excitation Fluorescence Imaging Global Enhancement"
        year="2023"
        type="journal"
        tags="ai,imaging"
        search="fluorescence imaging global enhancement deep learning"
        authors="Zhibo Xiao, Yinghan Guan, Wei Hou*, <span class='author-me'>Yuanjie Gu</span>*, Shouyu Wang*"
        venue="Optics Letters"
        meta="<span><i class='fas fa-calendar'></i> 2023</span><span><i class='fas fa-book'></i> Opt. Lett.</span><span><i class='fas fa-star'></i> IF: ~3.6</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib12"
        bibtexKey="xiao2023deepgamma"
        bibtexContent="@article{xiao2023deepgamma, title={Deep-Gamma: Deep Low-excitation Fluorescence Imaging Global Enhancement}, author={Xiao, Zhibo and Guan, Yinghan and Hou, Wei and Gu, Yuanjie and Wang, Shouyu}, journal={Optics Letters}, volume={48}, number={9}, pages={2496-2499}, year={2023}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib12')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    <!-- ================================================================================== -->
    <!-- 2022 Papers -->
    <!-- ================================================================================== -->
    {{< publication_item
        title="Deep Low-excitation Fluorescence Imaging Enhancement"
        year="2022"
        type="journal"
        tags="ai,imaging"
        search="fluorescence imaging enhancement low-excitation"
        authors="<span class='author-me'>Yuanjie Gu</span>#, Zhibo Xiao#, Wei Hou, Cheng Liu, Ying Jin, Shouyu Wang*"
        venue="Optics Letters"
        meta="<span><i class='fas fa-calendar'></i> 2022</span><span><i class='fas fa-book'></i> Opt. Lett.</span><span><i class='fas fa-star'></i> IF: ~3.6</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib6"
        bibtexKey="gu2022deep"
        bibtexContent="@article{gu2022deep, title={Deep Low-excitation Fluorescence Imaging Enhancement}, author={Gu, Yuanjie and Xiao, Zhibo and Hou, Wei and Liu, Cheng and Jin, Ying and Wang, Shouyu}, journal={Optics Letters}, volume={47}, number={16}, pages={4175-4178}, year={2022}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib6')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Deep Fusion Prior for Plenoptic Super-resolution All-in-focus Imaging"
        year="2022"
        type="journal"
        tags="ai,imaging"
        search="plenoptic super-resolution all-in-focus imaging"
        authors="<span class='author-me'>Yuanjie Gu</span>, Yinghan Guan, Zhibo Xiao, Haoran Dai, Cheng Liu, Shouyu Wang*"
        venue="Optical Engineering"
        meta="<span><i class='fas fa-calendar'></i> 2022</span><span><i class='fas fa-book'></i> Opt. Eng.</span><span><i class='fas fa-star'></i> IF: ~1.3</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib8"
        bibtexKey="gu2022deepfusion"
        bibtexContent="@article{gu2022deepfusion, title={Deep Fusion Prior for Plenoptic Super-resolution All-in-focus Imaging}, author={Gu, Yuanjie and Guan, Yinghan and Xiao, Zhibo and Dai, Haoran and Liu, Cheng and Wang, Shouyu}, journal={Optical Engineering}, volume={61}, number={12}, pages={123103}, year={2022}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib8')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="OpenRefocus: An Open-source Qt-based Tool for Light Field Parallel Refocusing"
        year="2022"
        type="journal"
        tags="software,imaging"
        search="light field refocusing open-source"
        authors="<span class='author-me'>Yuanjie Gu</span>, Miao Yu, Lingyu Ai, Zhilong Jiang, Xiaoliang He, Yan Kong, Shouyu Wang*"
        venue="Optical Engineering"
        meta="<span><i class='fas fa-calendar'></i> 2022</span><span><i class='fas fa-book'></i> Opt. Eng.</span><span><i class='fas fa-star'></i> IF: ~1.3</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib9"
        bibtexKey="gu2022openrefocus"
        bibtexContent="@article{gu2022openrefocus, title={OpenRefocus: An Open-source Qt-based Tool for Light Field Parallel Refocusing}, author={Gu, Yuanjie and Yu, Miao and Ai, Lingyu and Jiang, Zhilong and He, Xiaoliang and Kong, Yan and Wang, Shouyu}, journal={Optical Engineering}, volume={61}, number={6}, pages={063108}, year={2022}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib9')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    {{< publication_item
        title="Automatic Whole Blood Cell Analysis from Blood Smear using Label-free Multi-modal Imaging with Deep Neural Networks"
        year="2022"
        type="journal"
        tags="ai,medical"
        search="blood cell analysis multi-modal imaging deep learning"
        authors="Chao Chen, <span class='author-me'>Yuanjie Gu</span>, Zhibo Xiao, Hailun Wang, Xiaoliang He, Zhilong Jiang, Yan Kong, Cheng Liu, Liang Xue, Javier Vargas, Shouyu Wang*"
        venue="Analytica Chimica Acta"
        meta="<span><i class='fas fa-calendar'></i> 2022</span><span><i class='fas fa-book'></i> Anal. Chim. Acta</span><span><i class='fas fa-star'></i> IF: ~6.2</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib17"
        bibtexKey="chen2022automatic"
        bibtexContent="@article{chen2022automatic, title={Automatic Whole Blood Cell Analysis from Blood Smear using Label-free Multi-modal Imaging with Deep Neural Networks}, author={Chen, Chao and Gu, Yuanjie and Xiao, Zhibo and Wang, Hailun and He, Xiaoliang and Jiang, Zhilong and Kong, Yan and Liu, Cheng and Xue, Liang and Vargas, Javier and Wang, Shouyu}, journal={Analytica Chimica Acta}, volume={1229}, pages={340401}, year={2022}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib17')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}
    <!-- ================================================================================== -->
    <!-- 2021 Papers -->
    <!-- ================================================================================== -->
    {{< publication_item
        title="REPAID: Resolution-enhanced Plenoptic All-in-focus Imaging using Deep Neural Networks"
        year="2021"
        type="journal"
        tags="ai,imaging"
        search="plenoptic all-in-focus imaging deep learning"
        authors="Miao Yu#, <span class='author-me'>Yuanjie Gu</span>#, Zhilong Jiang, Xiaoliang He, Yan Kong, Cheng Liu, Shouyu Wang*"
        venue="Optics Letters"
        meta="<span><i class='fas fa-calendar'></i> 2021</span><span><i class='fas fa-book'></i> Opt. Lett.</span><span><i class='fas fa-star'></i> IF: ~3.6</span><span><i class='fas fa-quote-right'></i> Citations: TBD</span>"
        bibtexId="bib11"
        bibtexKey="yu2021repaid"
        bibtexContent="@article{yu2021repaid, title={REPAID: Resolution-enhanced Plenoptic All-in-focus Imaging using Deep Neural Networks}, author={Yu, Miao and Gu, Yuanjie and Jiang, Zhilong and He, Xiaoliang and Kong, Yan and Liu, Cheng and Wang, Shouyu}, journal={Optics Letters}, volume={46}, number={12}, pages={2896-2899}, year={2021}}"
    >}}
        <a href="#" class="btn-action btn-primary"><i class="fas fa-file-pdf"></i> PDF</a>
        <a href="#" class="btn-action"><i class="fab fa-github"></i> Code</a>
        <button class="btn-action" onclick="toggleBibtex('bib11')"><i class="fas fa-quote-right"></i> BibTeX</button>
        <a href="#" class="btn-action"><i class="fas fa-external-link-alt"></i> arXiv</a>
    {{< /publication_item >}}

</div>

</div>

<!-- 引入 JavaScript -->
{{< publications_js >}}