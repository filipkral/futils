dataframe2htmltable<-function(x, file, htmlclass="", htmlid="", htmlhead="<head><title>Table</title></head>", doctypeline="<!DOCTYPE html>", tablestyle="", tdstyle="", tableonly=F, useth=F){
	# Write data frame to html file and return path to the file on success
	# Note that no formatting is applied to numbers, x has to be formatted already as you want it to appear
	# x: input data frame
	# file: output html file
	# htmlclass: optional class to be used for the table
	# htmlid: optional id to be used for the table
	# htmhead: optional string to be used in place of html "<head>...</head>"
	# doctypeline: optional doctype line
	# tablestyle: can be used to include inline css style; no style added by default, use for example stylestring="border: 1px solid black"
	# tdstyle: like tablestyle but applied to <td> tag
	# tableonly: default is F which will write a full html page, only "<table>...</table>" will be written if tableonly=T
	# useth: default is F, names of columns will not be added; useth will add column names as <tr><th>...</th></tr>
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
	tablestylestring<-""
	if(tablestyle!=""){ 
		tablestylestring<-paste(" style=\"", tablestyle, "\"", sep="")
	}
	tdstylestring<-""
	if(tdstyle!=""){ 
		tdstylestring<-paste(" style=\"", tdstyle, "\"", sep="")
	}
	cat(paste("\n<table", classstring, idstring, tablestylestring,">", sep=""), file=file, append=(!tableonly))
	if(useth){
		cat(paste("\n<tr>", paste("<th>", names(x), "</th>", sep="", collapse=""), "</tr>", sep=""), file=file, append=T)
	}
	for(i in 1:nrow(x)){
		cat(paste("\n<tr>", paste(paste("<td", tdstylestring, ">", sep=""), x[i,], "</td>", sep="", collapse=""), "</tr>", sep=""), file=file, append=T)
	}
	cat(paste("\n</table>", sep=""), file=file, append=T)
	if(!tableonly){
		cat("\n</html>", file=file, append=T)
	}
	return(file)
}
