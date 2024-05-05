# $NetBSD$

DISTNAME=	PythonExtensions-2.2.6
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_PYPI:=P/PythonExtensions/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/PythonExtensions/
COMMENT=	Strongly typed classes with multiple built-in helper functions
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-aiofiles>=22.1.0:../../devel/py-aiofiles
DEPENDS+=	${PYPKGPREFIX}-aiohttp>=3.8.3:../../www/py-aiohttp
DEPENDS+=	${PYPKGPREFIX}-attr>=0.3.2:../../pkgsrc_myownpkgs/py-attr
DEPENDS+=	${PYPKGPREFIX}-cattrs>=22.2.0:../../devel/py-cattrs
DEPENDS+=	${PYPKGPREFIX}-cryptography>=38.0.1:../../security/py-cryptography
DEPENDS+=	${PYPKGPREFIX}-multidict>=6.0.2:../../databases/py-multidict
DEPENDS+=	${PYPKGPREFIX}-Pillow>=9.2.0:../../graphics/py-Pillow
DEPENDS+=	${PYPKGPREFIX}-prettyprinter>=0.18.0:../../pkgsrc_myownpkgs/py-prettyprinter
DEPENDS+=	${PYPKGPREFIX}-psutil>=5.9.3:../../sysutils/py-psutil
DEPENDS+=	${PYPKGPREFIX}-requests>=2.28.1:../../devel/py-requests
#DEPENDS+=	${PYPKGPREFIX}-tk_html_widgets>=0.4.0:../../pkgsrc_myownpkgs/py-tk_html_widgets
DEPENDS+=	${PYPKGPREFIX}-yarl>=1.8.1:../../www/py-yarl

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
