# $NetBSD$

DISTNAME=	prettyprinter-0.18.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/prettyprinter/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/tommikaikkonen/prettyprinter
COMMENT=	Syntax-highlighting, declarative and composable pretty printer
LICENSE=	mit

TOOL_DEPENDS+=	${PYPKGPREFIX}-test-runner>=3.0:../../devel/py-test-runner
DEPENDS+=	${PYPKGPREFIX}-pygments>=2.2.0:../../textproc/py-pygments
DEPENDS+=	${PYPKGPREFIX}-colorful>=0.4.0:../../pkgsrc_myownpkgs/py-colorful

#TEST_DEPENDS+=	${PYPKGPREFIX}-django>=1.10.8:../../www/py-django
#TEST_DEPENDS+=	# TODO: IPython==6.2.1>=0
#TEST_DEPENDS+=	# TODO: attrs==17.4.0>=0
#TEST_DEPENDS+=	# TODO: dataclasses==0.6>=0
#TEST_DEPENDS+=	# TODO: hypothesis==3.33.0>=0
#TEST_DEPENDS+=	# TODO: pytest==4.3.0>=0
#TEST_DEPENDS+=	# TODO: pytest-django==3.4.7>=0
#TEST_DEPENDS+=	# TODO: pytest-pythonpath==0.7.3>=0
#TEST_DEPENDS+=	# TODO: pytz==2017.3>=0
#TEST_DEPENDS+=	# TODO: requests==2.21.0>=0
#TEST_DEPENDS+=	# TODO: tox-pyenv==1.1.0>=0

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=0
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
