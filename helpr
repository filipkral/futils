dataframe2htmltable<-function(x, file, htmlclass="", htmlid="", htmlhead="<head><title>Table</title></head>", doctypeline="<!DOCTYPE html>", tableonly=F){
  # Write data frame to html file and return path to the file on success
	# Note that no formatting is applied to numbers, x has to be formatted already as you want it to appear
	# x: input data frame
	# file: output html file
	# htmlclass: optional class to be used for the table
	# htmlid: optional id to be used for the table
	# htmhead: optional string to be used in place of html "<head>...</head>"
	# doctypeline: optional doctype line
	# tableonly: default is F which will write a full html page, only "<table>...</table>" will be written if tableonly=T
	if(!tableonly){
		cat(paste(doctypeline, "\n", htmlhead, sep=""), file=file)
	}
	classstring<-""
	if(htmlclass!=""){
		classstring<-paste(" class=\"", htmlclass, "\"", sep="")
	}
	idstring<-""
	if(htmlid!=""){
		idstring<-paste(" id=\"", htmlid, "\"", sep="")
	}
	cat(paste("\n<table", classstring, idstring, ">", sep=""), file=file, append=(!tableonly))
	for(i in 1:nrow(x)){
			cat(paste("\n<tr>", paste("<td>", d[i,], "</td>", sep="", collapse=""), "</tr>", sep=""), file=file, append=T)
	}
	cat(paste("\n</table>", sep=""), file=file, append=T)
	if(!tableonly){
		cat("\n</html>", file=file, append=T)
	}
	return(file)
}
