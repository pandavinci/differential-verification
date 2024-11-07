# Variables
METAHOME = vojteskas@skirit.ics.muni.cz:~
METAPATH = /DP
SGEHOME = istanek@merlin.fit.vutbr.cz:/mnt/matylda0/istanek
SGEPATH = /jobs

.PHONY: clean clean_scripts scripts pack upload upload_sge

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f scripts.zip dp.zip

clean_scripts:
	rm -rf scripts.zip scripts/*.sh

scripts:
	python script_generator.py

pack: scripts clean
	zip -r dp.zip classifiers datasets extractors feature_processors trainers config.py common.py parse_arguments.py train_and_eval.py eval.py requirements.txt
	zip -r scripts.zip scripts -i "*.sh"

upload: pack
	scp scripts.zip $(METAHOME)$(METAPATH)/scripts.zip
	scp dp.zip $(METAHOME)$(METAPATH)/dp.zip
	scp runner.sh $(METAHOME)$(METAPATH)/runner.sh

upload_sge: pack
	scp scripts.zip $(SGEHOME)$(SGEPATH)/scripts.zip
	scp dp.zip $(SGEHOME)$(SGEPATH)/dp.zip
	scp runner.sh $(SGEHOME)$(SGEPATH)/runner.sh

make download:
	scp -r $(METAHOME)$(METAPATH)/trained_models ./trained_models
