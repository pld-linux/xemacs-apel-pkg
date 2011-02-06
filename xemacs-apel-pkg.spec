Summary:	A Portable Emacs Library - used by XEmacs MIME support
Summary(pl.UTF-8):	Przenośna biblioteka Emacsa - używana przez obsługę MIME XEmacsa
Name:		xemacs-apel-pkg
%define 	srcname	apel
Version:	1.32
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	0c3f9d60d3bdaf4a7f4eaf2bdf656e84
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Portable Emacs Library. Used by XEmacs MIME support.

%description -l pl.UTF-8
Przenośna biblioteka Emacsa. Używana przez obsługę MIME dla XEmacsa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/apel/README.ja lisp/apel/README.en lisp/apel/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
