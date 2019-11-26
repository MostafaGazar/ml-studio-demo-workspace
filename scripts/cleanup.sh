echo "Do you want to delete temporary data files? [Y,n]"
read input
if [[ $input == "n" || $input == "N" ]]; then
    # Do nothing
else
    rm -r ../data/processed/*
    rm -r ../data/cache/*
    rm -r ../data/raw/*
fi

