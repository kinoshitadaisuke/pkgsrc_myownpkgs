# $NetBSD$

DISTNAME=	bqplot-0.12.45
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=b/bqplot/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/bqplot/
COMMENT=	Interactive plotting for the Jupyter notebook
LICENSE=	apache-2.0

BUILD_DEPENDS+=	${PYPKGPREFIX}-jupyter_packaging>=0.12.2:../../devel/py-jupyter_packaging
BUILD_DEPENDS+=	${PYPKGPREFIX}-jupyterlab>=4.0:../../www/py-jupyterlab
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=40.8.0:../../devel/py-setuptools

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
