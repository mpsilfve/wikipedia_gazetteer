pages_fixed_infoboxes:pages_articles_fi.xml
	cat $^ | ./fix_infoboxes.sh > $@

infoboxes:pages_fixed_infoboxes
	cat $^ | python3 get_infoboxes.py > $@

info_categories:infoboxes
	cat $^ | python3 extract_info_category.py > $@

redirects:pages_fixed_infoboxes
	cat $^ | python3 get_redirects.py > $@

fi_wikipedia_gazetteer.pkl:info_categories redirects
	python3 add_redirects.py $^ $@ 