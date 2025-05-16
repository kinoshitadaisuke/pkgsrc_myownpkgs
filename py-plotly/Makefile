# $NetBSD$

DISTNAME=	plotly-6.1.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	graphics python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/plotly/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/plotly/
COMMENT=	Interactive, open-source, and browser-based graphing library
LICENSE=	mit

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools

DEPENDS+=	nodejs>=18:../../lang/nodejs
DEPENDS+=	${PYPKGPREFIX}-pip>=22.3.1:../../devel/py-pip
DEPENDS+=	${PYPKGPREFIX}-pandas>=0:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-black>=0:../../textproc/py-black
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-tenacity>=0:../../devel/py-tenacity
DEPENDS+=	${PYPKGPREFIX}-inflect>=0:../../lang/py-inflect
DEPENDS+=	${PYPKGPREFIX}-jupyterlab>=0:../../www/py-jupyterlab
DEPENDS+=	${PYPKGPREFIX}-ipywidgets>=0:../../www/py-ipywidgets
DEPENDS+=	${PYPKGPREFIX}-statsmodels>=0:../../math/py-statsmodels
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-twine>=0:../../net/py-twine
DEPENDS+=	${PYPKGPREFIX}-algoliasearch>=1.20:../../pkgsrc_myownpkgs/py-algoliasearch

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
