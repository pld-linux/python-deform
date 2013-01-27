#
# TODO
# - use system tiny_mce package
# - jquery, jquery-ui

# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define 	module	deform
Summary:	Python HTML form generation library
Name:		python-%{module}
Version:	0.9.6
Release:	1
# Some CSS and code (in the static directory) is provided via a Creative Commons license.  (see LICENSE.txt)
License:	BSD-derived (http://www.repoze.org/LICENSE.txt), CC BY 3.0 (assets)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/d/deform/%{module}-%{version}.tar.gz
# Source0-md5:	faf9054ad7c89457fe3ae1e3c0c15b97
URL:		http://docs.pylonsproject.org/projects/deform/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	pythonegg(peppercorn) >= 0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
deform is a Python HTML form generation library.

The design of deform is heavily influenced by the formish form
generation library. Some might even say it's a shameless rip-off; this
would not be completely inaccurate. It differs from formish mostly in
ways that make the implementation (arguably) simpler and smaller.

deform uses Colander as a schema library, Peppercorn as a form control
deserialization library, and Chameleon to perform HTML templating.

deform depends only on Peppercorn, Colander, Chameleon and an
internationalization library named translationstring, so it may be
used in most web frameworks (or antiframeworks) as a result.

Alternate templating languages may be used, as long as all templates
are translated from the native Chameleon templates to your templating
system of choice and a suitable renderer is supplied to deform.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/locale/%{module}.pot
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/locale/*/LC_MESSAGES/%{module}.po

install -d $RPM_BUILD_ROOT%{_localedir}
mv $RPM_BUILD_ROOT{%{py_sitescriptdir}/%{module}/locale/*,%{_localedir}}
rmdir $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/locale
# TODO: patch that the symlink won't be needed
ln -s %{_localedir} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/locale

mv $RPM_BUILD_ROOT/usr/share/locale/{de_DE,de}

%find_lang %{module}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{module}.lang
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt RESEARCH.txt TODO.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
%{py_sitescriptdir}/%{module}/locale
%{py_sitescriptdir}/%{module}/templates
%dir %{py_sitescriptdir}/%{module}/static
%dir %{py_sitescriptdir}/%{module}/static/css
%{py_sitescriptdir}/%{module}/static/css/beautify.css
%{py_sitescriptdir}/%{module}/static/css/fieldbg.gif
%{py_sitescriptdir}/%{module}/static/css/form.css
%{py_sitescriptdir}/%{module}/static/css/jquery-ui-timepicker-addon.css
%{py_sitescriptdir}/%{module}/static/css/jquery.autocomplete.css
%{py_sitescriptdir}/%{module}/static/css/next.gif
%{py_sitescriptdir}/%{module}/static/css/prev.gif
%{py_sitescriptdir}/%{module}/static/css/ui-lightness
%dir %{py_sitescriptdir}/%{module}/static/scripts
%{py_sitescriptdir}/%{module}/static/scripts/deform.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery-1.4.2.min.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery-1.7.2.min.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery-ui-1.8.11.custom.min.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery-ui-timepicker-addon.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery.form-3.09.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery.form.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery.maskMoney-1.4.1.js
%{py_sitescriptdir}/%{module}/static/scripts/jquery.maskedinput-1.2.2.min.js
%{py_sitescriptdir}/%{module}/static/tinymce
